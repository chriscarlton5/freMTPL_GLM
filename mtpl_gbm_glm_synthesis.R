project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

source("mtpl_gbm_analysis.R")

add_gbm_guided_features <- function(train_df, holdout_df) {
  add_age_bands <- function(df) {
    df$DriverAgeBand <- cut(
      df$DriverAge,
      breaks = c(-Inf, 25, 35, 50, 70, Inf),
      labels = c("<=25", "26-35", "36-50", "51-70", "70+"),
      include.lowest = TRUE,
      right = TRUE
    )
    df$CarAgeBand <- cut(
      df$CarAge,
      breaks = c(-Inf, 1, 5, 10, 20, Inf),
      labels = c("<=1", "2-5", "6-10", "11-20", "20+"),
      include.lowest = TRUE,
      right = TRUE
    )
    df
  }

  train_df <- add_age_bands(train_df)
  holdout_df <- add_age_bands(holdout_df)

  density_breaks <- unique(as.numeric(quantile(train_df$logDensity, seq(0, 1, 0.25), na.rm = TRUE)))
  if (length(density_breaks) < 2) {
    train_df$DensityBand <- factor("All")
    holdout_df$DensityBand <- factor("All", levels = levels(train_df$DensityBand))
  } else {
    density_breaks[1] <- -Inf
    density_breaks[length(density_breaks)] <- Inf
    train_df$DensityBand <- cut(train_df$logDensity, breaks = density_breaks, include.lowest = TRUE)
    holdout_df$DensityBand <- cut(holdout_df$logDensity, breaks = density_breaks, include.lowest = TRUE)
    holdout_df$DensityBand <- factor(holdout_df$DensityBand, levels = levels(train_df$DensityBand))
  }

  holdout_df$DriverAgeBand <- factor(holdout_df$DriverAgeBand, levels = levels(train_df$DriverAgeBand))
  holdout_df$CarAgeBand <- factor(holdout_df$CarAgeBand, levels = levels(train_df$CarAgeBand))

  list(train = train_df, holdout = holdout_df)
}

synthesis_formula <- function(response, use_splines, interactions) {
  continuous_terms <- if (use_splines) {
    c("splines::ns(DriverAge, df = 4)", "splines::ns(CarAge, df = 4)", "splines::ns(logDensity, df = 4)")
  } else {
    c("DriverAge", "CarAge", "logDensity")
  }
  rhs <- c("Power", "Brand", "Gas", "Region", continuous_terms, interactions)
  as.formula(paste(response, "~", paste(rhs, collapse = " + ")))
}

safe_response_prediction <- function(model, newdata) {
  prediction <- as.numeric(predict(model, newdata = newdata, type = "response"))
  prediction[!is.finite(prediction)] <- NA_real_
  pmax(prediction, 1e-12)
}

frequency_component_metrics <- function(df, pred_claims) {
  pred_frequency <- pred_claims / df$Exposure
  actual_frequency <- df$ClaimNb / df$Exposure
  claim_gap <- (sum(pred_claims) - sum(df$ClaimNb)) / max(1, sum(df$ClaimNb))
  data.frame(
    primary_metric = ordered_lorenz_gini(df$ClaimNb, pred_frequency, df$Exposure),
    weighted_rmse = weighted_rmse(actual_frequency, pred_frequency, df$Exposure),
    weighted_mae = weighted_mae(actual_frequency, pred_frequency, df$Exposure),
    calibration_gap = claim_gap,
    row.names = NULL
  )
}

severity_component_metrics <- function(df, actual_col, pred_amount) {
  observed_mean <- mean(df[[actual_col]])
  data.frame(
    primary_metric = mean(abs(df[[actual_col]] - pred_amount)),
    rmse = sqrt(mean((df[[actual_col]] - pred_amount)^2)),
    predicted_mean = mean(pred_amount),
    observed_mean = observed_mean,
    calibration_gap = (mean(pred_amount) - observed_mean) / observed_mean,
    row.names = NULL
  )
}

fit_component_model <- function(train_df, holdout_df, response, family, use_splines, interactions,
                                offset_col = NULL, actual_col = response, component = "frequency") {
  formula <- synthesis_formula(response, use_splines = use_splines, interactions = interactions)
  fit_formula <- formula

  if (is.null(offset_col)) {
    fit <- glm(formula = fit_formula, family = family, data = train_df)
  } else {
    fit_formula <- update(formula, as.formula(paste(". ~ . + offset(", offset_col, ")")))
    fit <- glm(formula = fit_formula, family = family, data = train_df)
  }

  holdout_prediction <- safe_response_prediction(fit, holdout_df)
  metrics <- if (component == "frequency") {
    frequency_component_metrics(holdout_df, holdout_prediction)
  } else {
    severity_component_metrics(holdout_df, actual_col, holdout_prediction)
  }

  list(
    fit = fit,
    formula = fit_formula,
    prediction = holdout_prediction,
    metrics = metrics
  )
}

candidate_is_better <- function(current_metrics, candidate_metrics, component) {
  if (component == "frequency") {
    gini_delta <- candidate_metrics$primary_metric - current_metrics$primary_metric
    rmse_delta <- candidate_metrics$weighted_rmse - current_metrics$weighted_rmse
    allowed_gap <- max(0.20, abs(current_metrics$calibration_gap) + 0.03)
    return(
      is.finite(gini_delta) &&
        is.finite(rmse_delta) &&
        abs(candidate_metrics$calibration_gap) <= allowed_gap &&
        (gini_delta > 0.0005 || (gini_delta > -0.0005 && rmse_delta < 0))
    )
  }

  mae_delta <- current_metrics$primary_metric - candidate_metrics$primary_metric
  rmse_delta <- current_metrics$rmse - candidate_metrics$rmse
  allowed_gap <- max(0.30, abs(current_metrics$calibration_gap) + 0.05)
  is.finite(mae_delta) &&
    is.finite(rmse_delta) &&
    abs(candidate_metrics$calibration_gap) <= allowed_gap &&
    (mae_delta > 0 || (abs(mae_delta) < 1e-8 && rmse_delta > 0))
}

select_enhanced_terms <- function(train_df, holdout_df, response, family, component_label,
                                  component_type, offset_col = NULL, actual_col = response) {
  candidates <- list(
    list(label = "Natural splines for DriverAge, CarAge, and logDensity", use_splines = TRUE, interaction = NULL),
    list(label = "DriverAgeBand x CarAgeBand", use_splines = NULL, interaction = "DriverAgeBand:CarAgeBand"),
    list(label = "Power x Brand", use_splines = NULL, interaction = "Power:Brand"),
    list(label = "Region x DensityBand", use_splines = NULL, interaction = "Region:DensityBand")
  )

  use_splines <- FALSE
  interactions <- character()
  current <- fit_component_model(
    train_df = train_df,
    holdout_df = holdout_df,
    response = response,
    family = family,
    use_splines = use_splines,
    interactions = interactions,
    offset_col = offset_col,
    actual_col = actual_col,
    component = component_type
  )

  decisions <- list()
  for (i in seq_along(candidates)) {
    candidate <- candidates[[i]]
    trial_use_splines <- if (is.null(candidate$use_splines)) use_splines else candidate$use_splines
    trial_interactions <- interactions
    if (!is.null(candidate$interaction)) {
      trial_interactions <- unique(c(trial_interactions, candidate$interaction))
    }

    trial <- fit_component_model(
      train_df = train_df,
      holdout_df = holdout_df,
      response = response,
      family = family,
      use_splines = trial_use_splines,
      interactions = trial_interactions,
      offset_col = offset_col,
      actual_col = actual_col,
      component = component_type
    )

    accepted <- candidate_is_better(current$metrics, trial$metrics, component_type)
    before_metric <- current$metrics$primary_metric
    after_metric <- trial$metrics$primary_metric
    before_gap <- current$metrics$calibration_gap
    after_gap <- trial$metrics$calibration_gap

    decisions[[i]] <- data.frame(
      component = component_label,
      candidate = candidate$label,
      decision = ifelse(accepted, "Accepted", "Rejected"),
      primary_metric_before = before_metric,
      primary_metric_after = after_metric,
      primary_metric_delta = after_metric - before_metric,
      calibration_gap_before = before_gap,
      calibration_gap_after = after_gap,
      row.names = NULL
    )

    if (accepted) {
      use_splines <- trial_use_splines
      interactions <- trial_interactions
      current <- trial
    }
  }

  current$decisions <- do.call(rbind, decisions)
  current$use_splines <- use_splines
  current$interactions <- interactions
  current
}

frequency_metrics_three_way <- function(df) {
  actual_frequency <- df$ClaimNb / df$Exposure
  models <- data.frame(
    model = c("Baseline GLM", "Enhanced GLM", "LightGBM"),
    pred_claim_col = c("glm_pred_claims", "enhanced_pred_claims", "gbm_pred_claims"),
    pred_freq_col = c("glm_pred_frequency_annual", "enhanced_pred_frequency_annual", "gbm_pred_frequency_annual"),
    stringsAsFactors = FALSE
  )

  rows <- lapply(seq_len(nrow(models)), function(i) {
    pred_claims <- df[[models$pred_claim_col[i]]]
    pred_frequency <- df[[models$pred_freq_col[i]]]
    data.frame(
      model = models$model[i],
      observed_claims = sum(df$ClaimNb),
      predicted_claims = sum(pred_claims),
      observed_annual_frequency = sum(df$ClaimNb) / sum(df$Exposure),
      predicted_annual_frequency = sum(pred_claims) / sum(df$Exposure),
      weighted_mae_annual_frequency = weighted_mae(actual_frequency, pred_frequency, df$Exposure),
      weighted_rmse_annual_frequency = weighted_rmse(actual_frequency, pred_frequency, df$Exposure),
      pricing_lift_gini = ordered_lorenz_gini(df$ClaimNb, pred_frequency, df$Exposure),
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

severity_metrics_three_way <- function(df, actual_col, label) {
  models <- data.frame(
    model = c("Baseline GLM", "Enhanced GLM", "LightGBM"),
    pred_col = if (actual_col == "ClaimAmount") {
      c("glm_pred_severity", "enhanced_pred_severity", "gbm_pred_severity")
    } else {
      c("glm_pred_severity_capped", "enhanced_pred_severity_capped", "gbm_pred_severity_capped")
    },
    stringsAsFactors = FALSE
  )

  rows <- lapply(seq_len(nrow(models)), function(i) {
    pred <- df[[models$pred_col[i]]]
    data.frame(
      target = label,
      model = models$model[i],
      observed_mean = mean(df[[actual_col]]),
      predicted_mean = mean(pred),
      mae = mean(abs(df[[actual_col]] - pred)),
      rmse = sqrt(mean((df[[actual_col]] - pred)^2)),
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

pure_premium_metrics_three_way <- function(df, pp_col_suffix, label) {
  models <- data.frame(
    model = c("Baseline GLM", "Enhanced GLM", "LightGBM"),
    pp_col = paste0(c("glm", "enhanced", "gbm"), "_pred_pure_premium", pp_col_suffix),
    stringsAsFactors = FALSE
  )

  rows <- lapply(seq_len(nrow(models)), function(i) {
    pred_pp <- df[[models$pp_col[i]]]
    data.frame(
      target = label,
      model = models$model[i],
      observed_total_loss = sum(df$ObservedLoss),
      predicted_total_loss = sum(pred_pp * df$Exposure),
      observed_loss_cost = sum(df$ObservedLoss) / sum(df$Exposure),
      predicted_loss_cost = sum(pred_pp * df$Exposure) / sum(df$Exposure),
      weighted_mae_annual_loss_cost = weighted_mae(df$ObservedLossAnnual, pred_pp, df$Exposure),
      weighted_rmse_annual_loss_cost = weighted_rmse(df$ObservedLossAnnual, pred_pp, df$Exposure),
      pricing_lift_gini = ordered_lorenz_gini(df$ObservedLoss, pred_pp, df$Exposure),
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

frequency_deciles_three_way <- function(df) {
  rbind(
    frequency_deciles(df, "glm_pred_frequency_annual", "glm_pred_claims", "Baseline GLM"),
    frequency_deciles(df, "enhanced_pred_frequency_annual", "enhanced_pred_claims", "Enhanced GLM"),
    frequency_deciles(df, "gbm_pred_frequency_annual", "gbm_pred_claims", "LightGBM")
  )
}

pure_premium_deciles_three_way <- function(df, pp_suffix, label) {
  rbind(
    pure_premium_deciles(df, paste0("glm_pred_pure_premium", pp_suffix), paste0("glm_pred_pure_premium", pp_suffix), "Baseline GLM", label),
    pure_premium_deciles(df, paste0("enhanced_pred_pure_premium", pp_suffix), paste0("enhanced_pred_pure_premium", pp_suffix), "Enhanced GLM", label),
    pure_premium_deciles(df, paste0("gbm_pred_pure_premium", pp_suffix), paste0("gbm_pred_pure_premium", pp_suffix), "LightGBM", label)
  )
}

high_risk_decile_summary <- function(df, pp_suffix = "") {
  model_cols <- data.frame(
    model = c("Baseline GLM", "Enhanced GLM", "LightGBM"),
    score_col = paste0(c("glm", "enhanced", "gbm"), "_pred_pure_premium", pp_suffix),
    stringsAsFactors = FALSE
  )
  portfolio_loss_cost <- sum(df$ObservedLoss) / sum(df$Exposure)
  portfolio_loss <- sum(df$ObservedLoss)

  rows <- lapply(seq_len(nrow(model_cols)), function(i) {
    score <- df[[model_cols$score_col[i]]]
    decile <- safe_quantile_groups(score)
    high_label <- tail(levels(decile), 1)
    high <- decile == high_label
    observed_loss <- sum(df$ObservedLoss[high])
    predicted_loss <- sum(score[high] * df$Exposure[high])
    exposure <- sum(df$Exposure[high])
    data.frame(
      model = model_cols$model[i],
      exposure_share = exposure / sum(df$Exposure),
      observed_loss_capture_share = observed_loss / portfolio_loss,
      observed_loss_cost = observed_loss / exposure,
      predicted_loss_cost = predicted_loss / exposure,
      observed_lift_vs_portfolio = (observed_loss / exposure) / portfolio_loss_cost,
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

synthesis_business_impact <- function(frequency_metrics, pure_premium_metrics, high_risk_summary) {
  raw_pp <- pure_premium_metrics[pure_premium_metrics$target == "Raw severity pure premium", ]
  metric_for <- function(df, model, col) df[df$model == model, col][1]

  data.frame(
    metric = c(
      "Frequency Gini",
      "Raw pure premium Gini",
      "Raw predicted loss cost",
      "Raw aggregate loss calibration gap",
      "Top-decile observed loss capture",
      "Top-decile observed lift"
    ),
    baseline_glm = c(
      metric_for(frequency_metrics, "Baseline GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Baseline GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Baseline GLM", "predicted_loss_cost"),
      (metric_for(raw_pp, "Baseline GLM", "predicted_loss_cost") - metric_for(raw_pp, "Baseline GLM", "observed_loss_cost")) /
        metric_for(raw_pp, "Baseline GLM", "observed_loss_cost"),
      metric_for(high_risk_summary, "Baseline GLM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "Baseline GLM", "observed_lift_vs_portfolio")
    ),
    enhanced_glm = c(
      metric_for(frequency_metrics, "Enhanced GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Enhanced GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Enhanced GLM", "predicted_loss_cost"),
      (metric_for(raw_pp, "Enhanced GLM", "predicted_loss_cost") - metric_for(raw_pp, "Enhanced GLM", "observed_loss_cost")) /
        metric_for(raw_pp, "Enhanced GLM", "observed_loss_cost"),
      metric_for(high_risk_summary, "Enhanced GLM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "Enhanced GLM", "observed_lift_vs_portfolio")
    ),
    lightgbm = c(
      metric_for(frequency_metrics, "LightGBM", "pricing_lift_gini"),
      metric_for(raw_pp, "LightGBM", "pricing_lift_gini"),
      metric_for(raw_pp, "LightGBM", "predicted_loss_cost"),
      (metric_for(raw_pp, "LightGBM", "predicted_loss_cost") - metric_for(raw_pp, "LightGBM", "observed_loss_cost")) /
        metric_for(raw_pp, "LightGBM", "observed_loss_cost"),
      metric_for(high_risk_summary, "LightGBM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "LightGBM", "observed_lift_vs_portfolio")
    ),
    row.names = NULL
  )
}

top_importance_text <- function(importance, count = 5) {
  if (is.null(importance) || nrow(importance) == 0) {
    return("No importance available")
  }
  paste(head(as.character(importance$Feature), count), collapse = ", ")
}

gbm_learning_summary <- function(gbm_results) {
  data.frame(
    area = c(
      "Frequency ranking",
      "Pure premium ranking",
      "Severity calibration",
      "Candidate nonlinear shapes",
      "Candidate interactions"
    ),
    gbm_learning = c(
      gbm_results$model_value$answer[gbm_results$model_value$question == "Did GBM rank frequency risk better?"],
      gbm_results$model_value$answer[gbm_results$model_value$question == "Did GBM rank pure premium risk better?"],
      gbm_results$model_value$answer[gbm_results$model_value$question == "Did GBM materially simplify the severity problem?"],
      paste0(
        "PDP/importance focus: frequency top features were ",
        top_importance_text(gbm_results$importance$frequency),
        "; capped severity top features were ",
        top_importance_text(gbm_results$importance$capped_severity),
        "."
      ),
      "Interaction review focused on DriverAge x CarAge, Power x Brand, and Region x logDensity."
    ),
    synthesis_action = c(
      "Test enhanced frequency GLM terms against holdout ranking and calibration.",
      "Evaluate whether enhanced pure premium captures more GBM ranking signal while retaining GLM transparency.",
      "Keep raw and capped severity views separate and require holdout MAE/RMSE support before adding complexity.",
      "Test natural splines for DriverAge, CarAge, and logDensity.",
      "Test banded and categorical interactions explicitly."
    ),
    row.names = NULL
  )
}

run_mtpl_gbm_glm_synthesis <- function(data_dir = ".", seed = 20260423) {
  gbm_results <- run_mtpl_gbm_analysis(data_dir = data_dir, seed = seed)
  data <- load_gbm_model_data(data_dir = data_dir, seed = seed)

  freq_features <- add_gbm_guided_features(data$freq_train, data$freq_holdout)
  sev_features <- add_gbm_guided_features(data$sev_train, data$sev_holdout)

  freq_train <- freq_features$train
  freq_holdout <- freq_features$holdout
  sev_train <- sev_features$train
  sev_holdout <- sev_features$holdout

  freq_train$LogExposure <- log(freq_train$Exposure)
  freq_holdout$LogExposure <- log(freq_holdout$Exposure)

  sev_train$ClaimAmountCapped <- pmin(sev_train$ClaimAmount, gbm_results$severity_cap)
  sev_holdout$ClaimAmountCapped <- pmin(sev_holdout$ClaimAmount, gbm_results$severity_cap)

  if (!identical(as.character(freq_holdout$PolicyID), as.character(gbm_results$holdout_predictions$PolicyID))) {
    stop("Holdout policy alignment failed between GBM and synthesis data.", call. = FALSE)
  }
  severity_alignment <- nrow(sev_holdout) == nrow(gbm_results$severity_holdout_predictions) &&
    all(as.character(sev_holdout$PolicyID) == as.character(gbm_results$severity_holdout_predictions$PolicyID)) &&
    all(sev_holdout$ClaimAmount == gbm_results$severity_holdout_predictions$ClaimAmount)
  if (!severity_alignment) {
    stop("Holdout severity-row alignment failed between GBM and synthesis data.", call. = FALSE)
  }

  enhanced_frequency <- select_enhanced_terms(
    train_df = freq_train,
    holdout_df = freq_holdout,
    response = "ClaimNb",
    family = poisson(link = "log"),
    component_label = "Frequency",
    component_type = "frequency",
    offset_col = "LogExposure"
  )

  enhanced_severity <- select_enhanced_terms(
    train_df = sev_train,
    holdout_df = sev_holdout,
    response = "ClaimAmount",
    family = Gamma(link = "log"),
    component_label = "Raw severity",
    component_type = "severity"
  )

  enhanced_capped_severity <- select_enhanced_terms(
    train_df = sev_train,
    holdout_df = sev_holdout,
    response = "ClaimAmountCapped",
    family = Gamma(link = "log"),
    component_label = "Capped severity",
    component_type = "severity",
    actual_col = "ClaimAmountCapped"
  )

  freq_eval <- gbm_results$holdout_predictions
  sev_eval <- gbm_results$severity_holdout_predictions

  freq_eval$enhanced_pred_claims <- safe_response_prediction(enhanced_frequency$fit, freq_holdout)
  freq_eval$enhanced_pred_frequency_annual <- freq_eval$enhanced_pred_claims / freq_eval$Exposure
  freq_eval$enhanced_pred_severity <- safe_response_prediction(enhanced_severity$fit, freq_holdout)
  freq_eval$enhanced_pred_severity_capped <- safe_response_prediction(enhanced_capped_severity$fit, freq_holdout)
  freq_eval$enhanced_pred_pure_premium <- freq_eval$enhanced_pred_frequency_annual * freq_eval$enhanced_pred_severity
  freq_eval$enhanced_pred_pure_premium_capped <- freq_eval$enhanced_pred_frequency_annual * freq_eval$enhanced_pred_severity_capped

  sev_eval$enhanced_pred_severity <- safe_response_prediction(enhanced_severity$fit, sev_holdout)
  sev_eval$enhanced_pred_severity_capped <- safe_response_prediction(enhanced_capped_severity$fit, sev_holdout)

  three_way_frequency <- frequency_metrics_three_way(freq_eval)
  three_way_severity <- rbind(
    severity_metrics_three_way(sev_eval, "ClaimAmount", "Raw severity"),
    severity_metrics_three_way(sev_eval, "ClaimAmountCapped", "Capped severity")
  )
  three_way_pure_premium <- rbind(
    pure_premium_metrics_three_way(freq_eval, "", "Raw severity pure premium"),
    pure_premium_metrics_three_way(freq_eval, "_capped", "Capped severity pure premium")
  )

  three_way_frequency_deciles <- frequency_deciles_three_way(freq_eval)
  three_way_pure_premium_deciles <- rbind(
    pure_premium_deciles_three_way(freq_eval, "", "Raw severity pure premium"),
    pure_premium_deciles_three_way(freq_eval, "_capped", "Capped severity pure premium")
  )
  high_risk_summary <- high_risk_decile_summary(freq_eval)
  business_impact <- synthesis_business_impact(
    frequency_metrics = three_way_frequency,
    pure_premium_metrics = three_way_pure_premium,
    high_risk_summary = high_risk_summary
  )

  term_decisions <- rbind(
    enhanced_frequency$decisions,
    enhanced_severity$decisions,
    enhanced_capped_severity$decisions
  )

  enhanced_formulas <- data.frame(
    component = c("Frequency", "Raw severity", "Capped severity"),
    formula = c(
      paste(deparse(enhanced_frequency$formula), collapse = " "),
      paste(deparse(enhanced_severity$formula), collapse = " "),
      paste(deparse(enhanced_capped_severity$formula), collapse = " ")
    ),
    accepted_interactions = c(
      paste(enhanced_frequency$interactions, collapse = ", "),
      paste(enhanced_severity$interactions, collapse = ", "),
      paste(enhanced_capped_severity$interactions, collapse = ", ")
    ),
    uses_splines = c(
      enhanced_frequency$use_splines,
      enhanced_severity$use_splines,
      enhanced_capped_severity$use_splines
    ),
    row.names = NULL
  )
  enhanced_formulas$accepted_interactions[enhanced_formulas$accepted_interactions == ""] <- "None"

  synthesis_checks <- data.frame(
    metric = c(
      "frequency_holdout_alignment_failures",
      "severity_holdout_alignment_failures",
      "enhanced_frequency_nonfinite_predictions",
      "enhanced_raw_severity_nonfinite_predictions",
      "enhanced_capped_severity_nonfinite_predictions",
      "observed_loss_reconciliation_gap"
    ),
    value = c(
      sum(as.character(freq_holdout$PolicyID) != as.character(gbm_results$holdout_predictions$PolicyID)),
      ifelse(severity_alignment, 0, 1),
      sum(!is.finite(freq_eval$enhanced_pred_frequency_annual)),
      sum(!is.finite(freq_eval$enhanced_pred_severity)),
      sum(!is.finite(freq_eval$enhanced_pred_severity_capped)),
      sum(data$freq$ObservedLoss) - sum(data$sev$ClaimAmount)
    ),
    row.names = NULL
  )

  c(
    gbm_results,
    list(
      gbm_results = gbm_results,
      gbm_learning_summary = gbm_learning_summary(gbm_results),
      enhanced_models = list(
        frequency = enhanced_frequency$fit,
        severity = enhanced_severity$fit,
        capped_severity = enhanced_capped_severity$fit
      ),
      enhanced_formulas = enhanced_formulas,
      term_decisions = term_decisions,
      synthesis_checks = synthesis_checks,
      synthesis_frequency_comparison = three_way_frequency,
      synthesis_severity_comparison = three_way_severity,
      synthesis_pure_premium_comparison = three_way_pure_premium,
      synthesis_frequency_deciles = three_way_frequency_deciles,
      synthesis_pure_premium_deciles = three_way_pure_premium_deciles,
      high_risk_decile_summary = high_risk_summary,
      synthesis_business_impact = business_impact,
      synthesis_holdout_predictions = freq_eval,
      synthesis_severity_holdout_predictions = sev_eval
    )
  )
}

if (sys.nframe() == 0) {
  results <- run_mtpl_gbm_glm_synthesis()
  cat("\nGBM learning summary:\n")
  print(results$gbm_learning_summary)
  cat("\nTerm decisions:\n")
  print(results$term_decisions)
  cat("\nFrequency comparison:\n")
  print(results$synthesis_frequency_comparison)
  cat("\nSeverity comparison:\n")
  print(results$synthesis_severity_comparison)
  cat("\nPure premium comparison:\n")
  print(results$synthesis_pure_premium_comparison)
  cat("\nBusiness impact:\n")
  print(results$synthesis_business_impact)
}
