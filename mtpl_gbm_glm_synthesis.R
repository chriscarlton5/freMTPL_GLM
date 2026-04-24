project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

source("mtpl_gbm_analysis.R")

add_gbm_guided_feature_sets <- function(reference_df, datasets) {
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

  reference_df <- add_age_bands(reference_df)
  density_breaks <- unique(as.numeric(quantile(reference_df$logDensity, seq(0, 1, 0.25), na.rm = TRUE)))
  use_single_density_level <- length(density_breaks) < 2
  if (!use_single_density_level) {
    density_breaks[1] <- -Inf
    density_breaks[length(density_breaks)] <- Inf
    reference_df$DensityBand <- cut(reference_df$logDensity, breaks = density_breaks, include.lowest = TRUE)
  } else {
    reference_df$DensityBand <- factor("All")
  }

  driver_levels <- levels(reference_df$DriverAgeBand)
  car_levels <- levels(reference_df$CarAgeBand)
  density_levels <- levels(reference_df$DensityBand)

  apply_features <- function(df) {
    df <- add_age_bands(df)
    df$DriverAgeBand <- factor(df$DriverAgeBand, levels = driver_levels)
    df$CarAgeBand <- factor(df$CarAgeBand, levels = car_levels)
    if (use_single_density_level) {
      df$DensityBand <- factor("All", levels = density_levels)
    } else {
      df$DensityBand <- cut(df$logDensity, breaks = density_breaks, include.lowest = TRUE)
      df$DensityBand <- factor(df$DensityBand, levels = density_levels)
    }
    df
  }

  lapply(datasets, apply_features)
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

fit_selected_model <- function(train_df, response, family, use_splines, interactions, offset_col = NULL) {
  fit_formula <- synthesis_formula(response, use_splines = use_splines, interactions = interactions)
  if (!is.null(offset_col)) {
    fit_formula <- update(fit_formula, as.formula(paste(". ~ . + offset(", offset_col, ")")))
  }
  glm(formula = fit_formula, family = family, data = train_df)
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
  fit <- fit_selected_model(
    train_df = train_df,
    response = response,
    family = family,
    use_splines = use_splines,
    interactions = interactions,
    offset_col = offset_col
  )

  holdout_prediction <- safe_response_prediction(fit, holdout_df)
  metrics <- if (component == "frequency") {
    frequency_component_metrics(holdout_df, holdout_prediction)
  } else {
    severity_component_metrics(holdout_df, actual_col, holdout_prediction)
  }

  list(
    fit = fit,
    formula = formula(fit),
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

select_enhanced_terms <- function(train_df, validation_df, response, family, component_label,
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
    holdout_df = validation_df,
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
      holdout_df = validation_df,
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
      selection_sample = "Internal validation",
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

add_prediction_set <- function(freq_df, sev_df, models, prefix, model_type = "glm") {
  if (model_type == "gbm") {
    freq_annual <- pmax(predict(models$frequency, encode_features(freq_df)), 1e-12)
    freq_df[[paste0(prefix, "_pred_frequency_annual")]] <- freq_annual
    freq_df[[paste0(prefix, "_pred_claims")]] <- freq_annual * freq_df$Exposure
    sev_df[[paste0(prefix, "_pred_severity")]] <- pmax(predict(models$severity, encode_features(sev_df)), 1e-12)
    sev_df[[paste0(prefix, "_pred_severity_capped")]] <- pmax(predict(models$capped_severity, encode_features(sev_df)), 1e-12)
    freq_df[[paste0(prefix, "_pred_severity")]] <- pmax(predict(models$severity, encode_features(freq_df)), 1e-12)
    freq_df[[paste0(prefix, "_pred_severity_capped")]] <- pmax(predict(models$capped_severity, encode_features(freq_df)), 1e-12)
  } else {
    claims <- safe_response_prediction(models$frequency, freq_df)
    freq_df[[paste0(prefix, "_pred_claims")]] <- claims
    freq_df[[paste0(prefix, "_pred_frequency_annual")]] <- claims / freq_df$Exposure
    sev_df[[paste0(prefix, "_pred_severity")]] <- safe_response_prediction(models$severity, sev_df)
    sev_df[[paste0(prefix, "_pred_severity_capped")]] <- safe_response_prediction(models$capped_severity, sev_df)
    freq_df[[paste0(prefix, "_pred_severity")]] <- safe_response_prediction(models$severity, freq_df)
    freq_df[[paste0(prefix, "_pred_severity_capped")]] <- safe_response_prediction(models$capped_severity, freq_df)
  }

  freq_df[[paste0(prefix, "_pred_pure_premium")]] <-
    freq_df[[paste0(prefix, "_pred_frequency_annual")]] * freq_df[[paste0(prefix, "_pred_severity")]]
  freq_df[[paste0(prefix, "_pred_pure_premium_capped")]] <-
    freq_df[[paste0(prefix, "_pred_frequency_annual")]] * freq_df[[paste0(prefix, "_pred_severity_capped")]]

  list(freq = freq_df, severity = sev_df)
}

frequency_metrics_for_models <- function(df, models) {
  actual_frequency <- df$ClaimNb / df$Exposure
  rows <- lapply(seq_len(nrow(models)), function(i) {
    prefix <- models$prefix[i]
    pred_claims <- df[[paste0(prefix, "_pred_claims")]]
    pred_frequency <- df[[paste0(prefix, "_pred_frequency_annual")]]
    data.frame(
      model = models$model[i],
      observed_claims = sum(df$ClaimNb),
      predicted_claims = sum(pred_claims),
      observed_annual_frequency = sum(df$ClaimNb) / sum(df$Exposure),
      predicted_annual_frequency = sum(pred_claims) / sum(df$Exposure),
      weighted_mae_annual_frequency = weighted_mae(actual_frequency, pred_frequency, df$Exposure),
      weighted_rmse_annual_frequency = weighted_rmse(actual_frequency, pred_frequency, df$Exposure),
      pricing_lift_gini = ordered_lorenz_gini(df$ClaimNb, pred_frequency, df$Exposure),
      calibration_gap = (sum(pred_claims) - sum(df$ClaimNb)) / max(1, sum(df$ClaimNb)),
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

severity_metrics_for_models <- function(df, actual_col, label, models) {
  rows <- lapply(seq_len(nrow(models)), function(i) {
    prefix <- models$prefix[i]
    pred_col <- if (actual_col == "ClaimAmount") {
      paste0(prefix, "_pred_severity")
    } else {
      paste0(prefix, "_pred_severity_capped")
    }
    pred <- df[[pred_col]]
    observed_mean <- mean(df[[actual_col]])
    data.frame(
      target = label,
      model = models$model[i],
      observed_mean = observed_mean,
      predicted_mean = mean(pred),
      mae = mean(abs(df[[actual_col]] - pred)),
      rmse = sqrt(mean((df[[actual_col]] - pred)^2)),
      calibration_gap = (mean(pred) - observed_mean) / observed_mean,
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

pure_premium_metrics_for_models <- function(df, models, pp_suffix, label,
                                            observed_loss_col = "ObservedLoss",
                                            observed_loss_annual_col = "ObservedLossAnnual") {
  observed_loss <- df[[observed_loss_col]]
  observed_loss_annual <- df[[observed_loss_annual_col]]
  rows <- lapply(seq_len(nrow(models)), function(i) {
    pred_pp <- if ("pp_col" %in% names(models) && nzchar(models$pp_col[i])) {
      df[[models$pp_col[i]]]
    } else {
      df[[paste0(models$prefix[i], "_pred_pure_premium", pp_suffix)]]
    }
    predicted_loss <- pred_pp * df$Exposure
    observed_loss_cost <- sum(observed_loss) / sum(df$Exposure)
    predicted_loss_cost <- sum(predicted_loss) / sum(df$Exposure)
    data.frame(
      target = label,
      model = models$model[i],
      observed_total_loss = sum(observed_loss),
      predicted_total_loss = sum(predicted_loss),
      observed_loss_cost = observed_loss_cost,
      predicted_loss_cost = predicted_loss_cost,
      weighted_mae_annual_loss_cost = weighted_mae(observed_loss_annual, pred_pp, df$Exposure),
      weighted_rmse_annual_loss_cost = weighted_rmse(observed_loss_annual, pred_pp, df$Exposure),
      pricing_lift_gini = ordered_lorenz_gini(observed_loss, pred_pp, df$Exposure),
      calibration_gap = (predicted_loss_cost - observed_loss_cost) / observed_loss_cost,
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

frequency_deciles_for_models <- function(df, models) {
  rows <- lapply(seq_len(nrow(models)), function(i) {
    frequency_deciles(
      df,
      paste0(models$prefix[i], "_pred_frequency_annual"),
      paste0(models$prefix[i], "_pred_claims"),
      models$model[i]
    )
  })
  do.call(rbind, rows)
}

pure_premium_deciles_for_models <- function(df, models, pp_suffix, label, observed_loss_col = "ObservedLoss") {
  rows <- lapply(seq_len(nrow(models)), function(i) {
    pp_col <- if ("pp_col" %in% names(models) && nzchar(models$pp_col[i])) {
      models$pp_col[i]
    } else {
      paste0(models$prefix[i], "_pred_pure_premium", pp_suffix)
    }
    pure_premium_deciles(
      df,
      pp_col,
      pp_col,
      models$model[i],
      label,
      observed_loss_col = observed_loss_col
    )
  })
  do.call(rbind, rows)
}

safe_ratio <- function(numerator, denominator, fallback = 1) {
  if (!is.finite(numerator) || !is.finite(denominator) || abs(denominator) < 1e-12) {
    return(fallback)
  }
  numerator / denominator
}

component_calibration_factors <- function(freq_df, sev_df, models) {
  rows <- lapply(seq_len(nrow(models)), function(i) {
    prefix <- models$prefix[i]
    frequency_factor <- safe_ratio(sum(freq_df$ClaimNb), sum(freq_df[[paste0(prefix, "_pred_claims")]]))
    severity_factor <- safe_ratio(mean(sev_df$ClaimAmount), mean(sev_df[[paste0(prefix, "_pred_severity")]]))
    capped_severity_factor <- safe_ratio(
      mean(sev_df$ClaimAmountCapped),
      mean(sev_df[[paste0(prefix, "_pred_severity_capped")]])
    )
    data.frame(
      model = models$model[i],
      prefix = prefix,
      frequency_factor = frequency_factor,
      raw_severity_factor = severity_factor,
      capped_severity_factor = capped_severity_factor,
      raw_pure_premium_factor = frequency_factor * severity_factor,
      capped_pure_premium_factor = frequency_factor * capped_severity_factor,
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

apply_component_calibration <- function(freq_df, sev_df, factors) {
  for (i in seq_len(nrow(factors))) {
    prefix <- factors$prefix[i]
    cal_prefix <- paste0(prefix, "_cal")
    freq_factor <- factors$frequency_factor[i]
    sev_factor <- factors$raw_severity_factor[i]
    capped_factor <- factors$capped_severity_factor[i]

    freq_df[[paste0(cal_prefix, "_pred_claims")]] <- freq_df[[paste0(prefix, "_pred_claims")]] * freq_factor
    freq_df[[paste0(cal_prefix, "_pred_frequency_annual")]] <-
      freq_df[[paste0(cal_prefix, "_pred_claims")]] / freq_df$Exposure
    freq_df[[paste0(cal_prefix, "_pred_severity")]] <- freq_df[[paste0(prefix, "_pred_severity")]] * sev_factor
    freq_df[[paste0(cal_prefix, "_pred_severity_capped")]] <-
      freq_df[[paste0(prefix, "_pred_severity_capped")]] * capped_factor
    freq_df[[paste0(cal_prefix, "_pred_pure_premium")]] <-
      freq_df[[paste0(cal_prefix, "_pred_frequency_annual")]] *
        freq_df[[paste0(cal_prefix, "_pred_severity")]]
    freq_df[[paste0(cal_prefix, "_pred_pure_premium_capped")]] <-
      freq_df[[paste0(cal_prefix, "_pred_frequency_annual")]] *
        freq_df[[paste0(cal_prefix, "_pred_severity_capped")]]

    sev_df[[paste0(cal_prefix, "_pred_severity")]] <- sev_df[[paste0(prefix, "_pred_severity")]] * sev_factor
    sev_df[[paste0(cal_prefix, "_pred_severity_capped")]] <-
      sev_df[[paste0(prefix, "_pred_severity_capped")]] * capped_factor
  }
  list(freq = freq_df, severity = sev_df)
}

pure_premium_ae_deciles <- function(df, models, observed_loss_col = "ObservedLoss") {
  rows <- lapply(seq_len(nrow(models)), function(i) {
    pp_col <- if ("pp_col" %in% names(models) && nzchar(models$pp_col[i])) {
      models$pp_col[i]
    } else {
      paste0(models$prefix[i], "_pred_pure_premium")
    }
    decile <- safe_quantile_groups(df[[pp_col]])
    observed_loss <- tapply(df[[observed_loss_col]], decile, sum)
    predicted_loss <- tapply(df[[pp_col]] * df$Exposure, decile, sum)
    exposure <- tapply(df$Exposure, decile, sum)
    data.frame(
      model = models$model[i],
      decile = seq_along(observed_loss),
      exposure = as.numeric(exposure),
      observed_loss = as.numeric(observed_loss),
      predicted_loss = as.numeric(predicted_loss),
      observed_loss_cost = as.numeric(observed_loss / exposure),
      predicted_loss_cost = as.numeric(predicted_loss / exposure),
      actual_to_expected = as.numeric(observed_loss / pmax(predicted_loss, 1e-12)),
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

fit_isotonic_pp <- function(df, score_col, observed_loss_col = "ObservedLoss") {
  decile <- safe_quantile_groups(df[[score_col]])
  mean_score <- tapply(seq_along(df[[score_col]]), decile, function(idx) {
    weighted_mean(df[[score_col]][idx], df$Exposure[idx])
  })
  observed_loss <- tapply(df[[observed_loss_col]], decile, sum)
  exposure <- tapply(df$Exposure, decile, sum)
  observed_loss_cost <- as.numeric(observed_loss / exposure)

  ordered <- order(as.numeric(mean_score))
  x <- as.numeric(mean_score)[ordered]
  y <- observed_loss_cost[ordered]
  keep <- is.finite(x) & is.finite(y) & !duplicated(x)
  x <- x[keep]
  y <- y[keep]
  if (length(x) < 4 || length(unique(y)) < 2) {
    return(NULL)
  }
  iso <- isoreg(seq_along(y), y)
  fitted <- pmax(as.numeric(iso$yf), 1e-12)
  list(x = x, y = fitted)
}

predict_isotonic_pp <- function(calibrator, score) {
  if (is.null(calibrator)) {
    return(rep(NA_real_, length(score)))
  }
  approx(
    x = calibrator$x,
    y = calibrator$y,
    xout = score,
    rule = 2,
    ties = "ordered"
  )$y
}

select_blend_weight <- function(df, calibration_threshold = 0.05) {
  grid <- seq(0, 1, by = 0.05)
  rows <- lapply(grid, function(alpha) {
    pred <- alpha * df$enhanced_cal_pred_pure_premium + (1 - alpha) * df$gbm_cal_pred_pure_premium
    observed_loss_cost <- sum(df$ObservedLoss) / sum(df$Exposure)
    predicted_loss_cost <- sum(pred * df$Exposure) / sum(df$Exposure)
    data.frame(
      alpha_enhanced = alpha,
      alpha_lightgbm = 1 - alpha,
      observed_loss_cost = observed_loss_cost,
      predicted_loss_cost = predicted_loss_cost,
      calibration_gap = (predicted_loss_cost - observed_loss_cost) / observed_loss_cost,
      weighted_mae_annual_loss_cost = weighted_mae(df$ObservedLossAnnual, pred, df$Exposure),
      pricing_lift_gini = ordered_lorenz_gini(df$ObservedLoss, pred, df$Exposure),
      row.names = NULL
    )
  })
  blend_grid <- do.call(rbind, rows)
  blend_grid$acceptable_calibration <- abs(blend_grid$calibration_gap) <= calibration_threshold
  eligible <- blend_grid[blend_grid$acceptable_calibration, , drop = FALSE]
  if (nrow(eligible) == 0) {
    eligible <- blend_grid
  }
  selected_index <- order(-eligible$pricing_lift_gini, eligible$weighted_mae_annual_loss_cost)[1]
  selected <- eligible[selected_index, , drop = FALSE]
  blend_grid$selected <- blend_grid$alpha_enhanced == selected$alpha_enhanced
  list(grid = blend_grid, selected = selected)
}

add_blend_predictions <- function(freq_df, selected_blend) {
  alpha <- selected_blend$alpha_enhanced[1]
  freq_df$blend_cal_pred_pure_premium <-
    alpha * freq_df$enhanced_cal_pred_pure_premium + (1 - alpha) * freq_df$gbm_cal_pred_pure_premium
  freq_df$blend_cal_pred_pure_premium_capped <-
    alpha * freq_df$enhanced_cal_pred_pure_premium_capped + (1 - alpha) * freq_df$gbm_cal_pred_pure_premium_capped
  freq_df
}

high_risk_decile_summary <- function(df, models, pp_suffix = "", observed_loss_col = "ObservedLoss") {
  portfolio_loss_cost <- sum(df[[observed_loss_col]]) / sum(df$Exposure)
  portfolio_loss <- sum(df[[observed_loss_col]])

  rows <- lapply(seq_len(nrow(models)), function(i) {
    score_col <- if ("pp_col" %in% names(models) && nzchar(models$pp_col[i])) {
      models$pp_col[i]
    } else {
      paste0(models$prefix[i], "_pred_pure_premium", pp_suffix)
    }
    score <- df[[score_col]]
    decile <- safe_quantile_groups(score)
    high_label <- tail(levels(decile), 1)
    high <- decile == high_label
    observed_loss <- sum(df[[observed_loss_col]][high])
    predicted_loss <- sum(score[high] * df$Exposure[high])
    exposure <- sum(df$Exposure[high])
    data.frame(
      model = models$model[i],
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
      metric_for(raw_pp, "Baseline GLM", "calibration_gap"),
      metric_for(high_risk_summary, "Baseline GLM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "Baseline GLM", "observed_lift_vs_portfolio")
    ),
    enhanced_glm = c(
      metric_for(frequency_metrics, "Enhanced GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Enhanced GLM", "pricing_lift_gini"),
      metric_for(raw_pp, "Enhanced GLM", "predicted_loss_cost"),
      metric_for(raw_pp, "Enhanced GLM", "calibration_gap"),
      metric_for(high_risk_summary, "Enhanced GLM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "Enhanced GLM", "observed_lift_vs_portfolio")
    ),
    lightgbm = c(
      metric_for(frequency_metrics, "LightGBM", "pricing_lift_gini"),
      metric_for(raw_pp, "LightGBM", "pricing_lift_gini"),
      metric_for(raw_pp, "LightGBM", "predicted_loss_cost"),
      metric_for(raw_pp, "LightGBM", "calibration_gap"),
      metric_for(high_risk_summary, "LightGBM", "observed_loss_capture_share"),
      metric_for(high_risk_summary, "LightGBM", "observed_lift_vs_portfolio")
    ),
    row.names = NULL
  )
}

candidate_acceptance_table <- function(validation_metrics, holdout_metrics, uncalibrated_metrics) {
  baseline <- uncalibrated_metrics[
    uncalibrated_metrics$model == "Baseline GLM" &
      uncalibrated_metrics$target == "Raw severity pure premium",
    ,
    drop = FALSE
  ][1, ]
  enhanced <- uncalibrated_metrics[
    uncalibrated_metrics$model == "Enhanced GLM" &
      uncalibrated_metrics$target == "Raw severity pure premium",
    ,
    drop = FALSE
  ][1, ]

  candidate_models <- unique(holdout_metrics$model)
  rows <- lapply(candidate_models, function(model_name) {
    validation <- validation_metrics[validation_metrics$model == model_name, , drop = FALSE][1, ]
    holdout <- holdout_metrics[holdout_metrics$model == model_name, , drop = FALSE][1, ]
    calibration_improved <- abs(holdout$calibration_gap) < abs(enhanced$calibration_gap)
    gini_ok <- holdout$pricing_lift_gini >= max(
      baseline$pricing_lift_gini + 0.005,
      enhanced$pricing_lift_gini - 0.005
    )
    mae_ok <- holdout$weighted_mae_annual_loss_cost <= enhanced$weighted_mae_annual_loss_cost * 1.01
    retained <- calibration_improved && gini_ok && mae_ok
    reason <- if (retained) {
      "Retained: final holdout calibration improved, Gini remained strong, and MAE stayed within tolerance."
    } else if (!calibration_improved) {
      "Rejected: final holdout aggregate calibration did not improve versus the uncalibrated enhanced GLM."
    } else if (!gini_ok) {
      "Rejected: final holdout Gini fell below the predeclared segmentation floor."
    } else {
      "Rejected: final holdout MAE worsened by more than the 1% tolerance."
    }
    data.frame(
      candidate = model_name,
      validation_calibration_gap = validation$calibration_gap,
      validation_gini = validation$pricing_lift_gini,
      validation_mae = validation$weighted_mae_annual_loss_cost,
      holdout_calibration_gap = holdout$calibration_gap,
      holdout_gini = holdout$pricing_lift_gini,
      holdout_mae = holdout$weighted_mae_annual_loss_cost,
      calibration_improved = calibration_improved,
      gini_ok = gini_ok,
      mae_ok = mae_ok,
      decision = ifelse(retained, "Retained", "Rejected"),
      reason = reason,
      row.names = NULL
    )
  })
  do.call(rbind, rows)
}

recommended_model_summary <- function(candidate_acceptance) {
  blend_row <- candidate_acceptance[candidate_acceptance$candidate == "Calibrated blend", , drop = FALSE]
  if (nrow(blend_row) == 1 && blend_row$decision == "Retained") {
    return(data.frame(
      selected_model = "Calibrated blend",
      reason = "The validation-selected blend also passed the final holdout acceptance gates.",
      row.names = NULL
    ))
  }
  retained <- candidate_acceptance[candidate_acceptance$decision == "Retained", , drop = FALSE]
  if (nrow(retained) > 0) {
    retained <- retained[order(abs(retained$holdout_calibration_gap), -retained$holdout_gini, retained$holdout_mae), ]
    return(data.frame(
      selected_model = retained$candidate[1],
      reason = "The calibrated blend did not pass all gates, so the best retained calibrated candidate is used.",
      row.names = NULL
    ))
  }
  data.frame(
    selected_model = "Uncalibrated enhanced GLM",
    reason = "No calibrated candidate passed the final holdout gates, so the modeling change is not retained as a pricing improvement.",
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
      "Test enhanced frequency GLM terms against internal validation ranking and calibration.",
      "Evaluate whether enhanced pure premium captures more GBM ranking signal while retaining GLM transparency.",
      "Keep raw and capped severity views separate and require validation MAE/RMSE support before adding complexity.",
      "Test natural splines for DriverAge, CarAge, and logDensity.",
      "Test banded and categorical interactions explicitly."
    ),
    row.names = NULL
  )
}

run_mtpl_gbm_glm_synthesis <- function(data_dir = ".", seed = 20260423) {
  gbm_results <- run_mtpl_gbm_analysis(data_dir = data_dir, seed = seed)
  data <- load_gbm_model_data(data_dir = data_dir, seed = seed)
  severity_cap <- gbm_results$severity_cap

  data$freq <- add_capped_loss_columns(data$freq, data$sev, severity_cap)
  freq_train_raw <- add_capped_loss_columns(data$freq_train, data$sev, severity_cap)
  freq_holdout_raw <- add_capped_loss_columns(data$freq_holdout, data$sev, severity_cap)
  sev_train_raw <- data$sev_train
  sev_holdout_raw <- data$sev_holdout

  freq_fit_raw <- freq_train_raw[freq_train_raw$gbm_split == "fit", ]
  freq_valid_raw <- freq_train_raw[freq_train_raw$gbm_split == "valid", ]
  sev_fit_raw <- sev_train_raw[sev_train_raw$gbm_split == "fit", ]
  sev_valid_raw <- sev_train_raw[sev_train_raw$gbm_split == "valid", ]

  freq_sets <- add_gbm_guided_feature_sets(
    reference_df = freq_fit_raw,
    datasets = list(
      fit = freq_fit_raw,
      valid = freq_valid_raw,
      train = freq_train_raw,
      holdout = freq_holdout_raw
    )
  )
  sev_sets <- add_gbm_guided_feature_sets(
    reference_df = sev_fit_raw,
    datasets = list(
      fit = sev_fit_raw,
      valid = sev_valid_raw,
      train = sev_train_raw,
      holdout = sev_holdout_raw
    )
  )

  freq_fit <- freq_sets$fit
  freq_valid <- freq_sets$valid
  freq_train <- freq_sets$train
  freq_holdout <- freq_sets$holdout
  sev_fit <- sev_sets$fit
  sev_valid <- sev_sets$valid
  sev_train <- sev_sets$train
  sev_holdout <- sev_sets$holdout

  freq_fit$LogExposure <- log(freq_fit$Exposure)
  freq_valid$LogExposure <- log(freq_valid$Exposure)
  freq_train$LogExposure <- log(freq_train$Exposure)
  freq_holdout$LogExposure <- log(freq_holdout$Exposure)

  sev_fit$ClaimAmountCapped <- pmin(sev_fit$ClaimAmount, severity_cap)
  sev_valid$ClaimAmountCapped <- pmin(sev_valid$ClaimAmount, severity_cap)
  sev_train$ClaimAmountCapped <- pmin(sev_train$ClaimAmount, severity_cap)
  sev_holdout$ClaimAmountCapped <- pmin(sev_holdout$ClaimAmount, severity_cap)

  if (!identical(as.character(freq_holdout$PolicyID), as.character(gbm_results$holdout_predictions$PolicyID))) {
    stop("Holdout policy alignment failed between GBM and synthesis data.", call. = FALSE)
  }
  severity_alignment <- nrow(sev_holdout) == nrow(gbm_results$severity_holdout_predictions) &&
    all(as.character(sev_holdout$PolicyID) == as.character(gbm_results$severity_holdout_predictions$PolicyID)) &&
    all(sev_holdout$ClaimAmount == gbm_results$severity_holdout_predictions$ClaimAmount)
  if (!severity_alignment) {
    stop("Holdout severity-row alignment failed between GBM and synthesis data.", call. = FALSE)
  }

  baseline_validation_models <- list(
    frequency = fit_selected_model(freq_fit, "ClaimNb", poisson(link = "log"), FALSE, character(), "LogExposure"),
    severity = fit_selected_model(sev_fit, "ClaimAmount", Gamma(link = "log"), FALSE, character()),
    capped_severity = fit_selected_model(sev_fit, "ClaimAmountCapped", Gamma(link = "log"), FALSE, character())
  )

  enhanced_frequency <- select_enhanced_terms(
    train_df = freq_fit,
    validation_df = freq_valid,
    response = "ClaimNb",
    family = poisson(link = "log"),
    component_label = "Frequency",
    component_type = "frequency",
    offset_col = "LogExposure"
  )

  enhanced_severity <- select_enhanced_terms(
    train_df = sev_fit,
    validation_df = sev_valid,
    response = "ClaimAmount",
    family = Gamma(link = "log"),
    component_label = "Raw severity",
    component_type = "severity"
  )

  enhanced_capped_severity <- select_enhanced_terms(
    train_df = sev_fit,
    validation_df = sev_valid,
    response = "ClaimAmountCapped",
    family = Gamma(link = "log"),
    component_label = "Capped severity",
    component_type = "severity",
    actual_col = "ClaimAmountCapped"
  )

  enhanced_validation_models <- list(
    frequency = enhanced_frequency$fit,
    severity = enhanced_severity$fit,
    capped_severity = enhanced_capped_severity$fit
  )
  enhanced_final_models <- list(
    frequency = fit_selected_model(
      freq_train,
      "ClaimNb",
      poisson(link = "log"),
      enhanced_frequency$use_splines,
      enhanced_frequency$interactions,
      "LogExposure"
    ),
    severity = fit_selected_model(
      sev_train,
      "ClaimAmount",
      Gamma(link = "log"),
      enhanced_severity$use_splines,
      enhanced_severity$interactions
    ),
    capped_severity = fit_selected_model(
      sev_train,
      "ClaimAmountCapped",
      Gamma(link = "log"),
      enhanced_capped_severity$use_splines,
      enhanced_capped_severity$interactions
    )
  )

  validation_eval <- add_prediction_set(freq_valid, sev_valid, baseline_validation_models, "glm", "glm")
  validation_eval <- add_prediction_set(validation_eval$freq, validation_eval$severity, enhanced_validation_models, "enhanced", "glm")
  validation_eval <- add_prediction_set(validation_eval$freq, validation_eval$severity, gbm_results$gbm_models, "gbm", "gbm")
  freq_valid_eval <- validation_eval$freq
  sev_valid_eval <- validation_eval$severity

  freq_eval <- gbm_results$holdout_predictions
  sev_eval <- gbm_results$severity_holdout_predictions
  enhanced_holdout <- add_prediction_set(freq_holdout, sev_holdout, enhanced_final_models, "enhanced", "glm")
  enhanced_freq_cols <- names(enhanced_holdout$freq)[grepl("^enhanced_", names(enhanced_holdout$freq))]
  enhanced_sev_cols <- names(enhanced_holdout$severity)[grepl("^enhanced_", names(enhanced_holdout$severity))]
  freq_eval[, enhanced_freq_cols] <- enhanced_holdout$freq[, enhanced_freq_cols]
  sev_eval[, enhanced_sev_cols] <- enhanced_holdout$severity[, enhanced_sev_cols]

  base_models <- data.frame(
    model = c("Baseline GLM", "Enhanced GLM", "LightGBM"),
    prefix = c("glm", "enhanced", "gbm"),
    stringsAsFactors = FALSE
  )

  validation_frequency <- frequency_metrics_for_models(freq_valid_eval, base_models)
  validation_severity <- rbind(
    severity_metrics_for_models(sev_valid_eval, "ClaimAmount", "Raw severity", base_models),
    severity_metrics_for_models(sev_valid_eval, "ClaimAmountCapped", "Capped severity", base_models)
  )
  validation_pure_premium <- rbind(
    pure_premium_metrics_for_models(freq_valid_eval, base_models, "", "Raw severity pure premium"),
    pure_premium_metrics_for_models(
      freq_valid_eval,
      base_models,
      "_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped",
      observed_loss_annual_col = "ObservedLossCappedAnnual"
    )
  )

  three_way_frequency <- frequency_metrics_for_models(freq_eval, base_models)
  three_way_severity <- rbind(
    severity_metrics_for_models(sev_eval, "ClaimAmount", "Raw severity", base_models),
    severity_metrics_for_models(sev_eval, "ClaimAmountCapped", "Capped severity", base_models)
  )
  three_way_pure_premium <- rbind(
    pure_premium_metrics_for_models(freq_eval, base_models, "", "Raw severity pure premium"),
    pure_premium_metrics_for_models(
      freq_eval,
      base_models,
      "_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped",
      observed_loss_annual_col = "ObservedLossCappedAnnual"
    )
  )

  calibration_factors <- component_calibration_factors(freq_valid_eval, sev_valid_eval, base_models)
  calibrated_valid <- apply_component_calibration(freq_valid_eval, sev_valid_eval, calibration_factors)
  calibrated_holdout <- apply_component_calibration(freq_eval, sev_eval, calibration_factors)
  freq_valid_eval <- calibrated_valid$freq
  sev_valid_eval <- calibrated_valid$severity
  freq_eval <- calibrated_holdout$freq
  sev_eval <- calibrated_holdout$severity

  calibrated_models <- data.frame(
    model = c("Baseline GLM calibrated", "Enhanced GLM calibrated", "LightGBM calibrated"),
    prefix = c("glm_cal", "enhanced_cal", "gbm_cal"),
    stringsAsFactors = FALSE
  )

  validation_calibrated_frequency <- frequency_metrics_for_models(freq_valid_eval, calibrated_models)
  validation_calibrated_severity <- rbind(
    severity_metrics_for_models(sev_valid_eval, "ClaimAmount", "Raw severity", calibrated_models),
    severity_metrics_for_models(sev_valid_eval, "ClaimAmountCapped", "Capped severity", calibrated_models)
  )
  validation_calibrated_pure_premium <- rbind(
    pure_premium_metrics_for_models(freq_valid_eval, calibrated_models, "", "Raw severity pure premium"),
    pure_premium_metrics_for_models(
      freq_valid_eval,
      calibrated_models,
      "_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped",
      observed_loss_annual_col = "ObservedLossCappedAnnual"
    )
  )

  holdout_calibrated_frequency <- frequency_metrics_for_models(freq_eval, calibrated_models)
  holdout_calibrated_severity <- rbind(
    severity_metrics_for_models(sev_eval, "ClaimAmount", "Raw severity", calibrated_models),
    severity_metrics_for_models(sev_eval, "ClaimAmountCapped", "Capped severity", calibrated_models)
  )
  holdout_calibrated_pure_premium <- rbind(
    pure_premium_metrics_for_models(freq_eval, calibrated_models, "", "Raw severity pure premium"),
    pure_premium_metrics_for_models(
      freq_eval,
      calibrated_models,
      "_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped",
      observed_loss_annual_col = "ObservedLossCappedAnnual"
    )
  )

  validation_ae_for_isotonic <- pure_premium_ae_deciles(
    freq_valid_eval,
    data.frame(model = "LightGBM calibrated", prefix = "gbm_cal", stringsAsFactors = FALSE)
  )
  ae_range <- range(validation_ae_for_isotonic$actual_to_expected, na.rm = TRUE)
  try_isotonic <- all(is.finite(ae_range)) && diff(ae_range) > 0.25
  isotonic_status <- data.frame(
    candidate = "LightGBM isotonic",
    attempted = try_isotonic,
    validation_ae_range = ifelse(all(is.finite(ae_range)), diff(ae_range), NA_real_),
    reason = ifelse(
      try_isotonic,
      "Attempted because validation decile A/E bias was non-uniform.",
      "Not attempted because validation decile A/E bias was not materially non-uniform."
    ),
    row.names = NULL
  )

  if (try_isotonic) {
    isotonic_calibrator <- fit_isotonic_pp(freq_valid_eval, "gbm_cal_pred_pure_premium")
    freq_valid_eval$gbm_iso_pred_pure_premium <-
      predict_isotonic_pp(isotonic_calibrator, freq_valid_eval$gbm_cal_pred_pure_premium)
    freq_eval$gbm_iso_pred_pure_premium <-
      predict_isotonic_pp(isotonic_calibrator, freq_eval$gbm_cal_pred_pure_premium)
  }

  blend_selection <- select_blend_weight(freq_valid_eval)
  freq_valid_eval <- add_blend_predictions(freq_valid_eval, blend_selection$selected)
  freq_eval <- add_blend_predictions(freq_eval, blend_selection$selected)

  candidate_models <- data.frame(
    model = c("Enhanced GLM calibrated", "LightGBM calibrated", "Calibrated blend"),
    prefix = c("enhanced_cal", "gbm_cal", "blend_cal"),
    pp_col = c(
      "enhanced_cal_pred_pure_premium",
      "gbm_cal_pred_pure_premium",
      "blend_cal_pred_pure_premium"
    ),
    stringsAsFactors = FALSE
  )
  if (try_isotonic && all(is.finite(freq_eval$gbm_iso_pred_pure_premium))) {
    candidate_models <- rbind(
      candidate_models,
      data.frame(
        model = "LightGBM isotonic",
        prefix = "gbm_iso",
        pp_col = "gbm_iso_pred_pure_premium",
        stringsAsFactors = FALSE
      )
    )
  }

  validation_candidate_metrics <- pure_premium_metrics_for_models(
    freq_valid_eval,
    candidate_models,
    "",
    "Raw severity pure premium"
  )
  holdout_candidate_metrics <- pure_premium_metrics_for_models(
    freq_eval,
    candidate_models,
    "",
    "Raw severity pure premium"
  )
  candidate_acceptance <- candidate_acceptance_table(
    validation_candidate_metrics,
    holdout_candidate_metrics,
    three_way_pure_premium
  )
  final_recommendation <- recommended_model_summary(candidate_acceptance)

  three_way_frequency_deciles <- frequency_deciles_for_models(freq_eval, base_models)
  three_way_pure_premium_deciles <- rbind(
    pure_premium_deciles_for_models(freq_eval, base_models, "", "Raw severity pure premium"),
    pure_premium_deciles_for_models(
      freq_eval,
      base_models,
      "_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped"
    )
  )
  high_risk_summary <- high_risk_decile_summary(freq_eval, base_models)
  candidate_high_risk_summary <- high_risk_decile_summary(freq_eval, candidate_models)
  raw_ae_deciles <- pure_premium_ae_deciles(freq_eval, rbind(
    data.frame(model = "Enhanced GLM", prefix = "enhanced", pp_col = "enhanced_pred_pure_premium", stringsAsFactors = FALSE),
    candidate_models
  ))

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
      paste(deparse(formula(enhanced_final_models$frequency)), collapse = " "),
      paste(deparse(formula(enhanced_final_models$severity)), collapse = " "),
      paste(deparse(formula(enhanced_final_models$capped_severity)), collapse = " ")
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

  capped_reconciliation_gap <- sum(freq_eval$ObservedLossCapped) -
    sum(pmin(sev_eval$ClaimAmount, severity_cap))
  synthesis_checks <- data.frame(
    metric = c(
      "frequency_holdout_alignment_failures",
      "severity_holdout_alignment_failures",
      "enhanced_frequency_nonfinite_predictions",
      "enhanced_raw_severity_nonfinite_predictions",
      "enhanced_capped_severity_nonfinite_predictions",
      "calibrated_prediction_nonfinite_values",
      "observed_loss_reconciliation_gap",
      "capped_observed_loss_reconciliation_gap"
    ),
    value = c(
      sum(as.character(freq_holdout$PolicyID) != as.character(gbm_results$holdout_predictions$PolicyID)),
      ifelse(severity_alignment, 0, 1),
      sum(!is.finite(freq_eval$enhanced_pred_frequency_annual)),
      sum(!is.finite(freq_eval$enhanced_pred_severity)),
      sum(!is.finite(freq_eval$enhanced_pred_severity_capped)),
      sum(!is.finite(as.matrix(freq_eval[, grep("_cal_|gbm_iso|blend_cal", names(freq_eval)), drop = FALSE]))),
      sum(data$freq$ObservedLoss) - sum(data$sev$ClaimAmount),
      capped_reconciliation_gap
    ),
    row.names = NULL
  )

  validation_design <- data.frame(
    sample = c("GBM/GLM fit", "Internal validation", "Final holdout"),
    role = c(
      "Fit LightGBM models and candidate enhanced GLM terms.",
      "Early stopping, enhanced-term selection, component calibration, isotonic trigger, and blend-weight selection.",
      "Final untouched measurement for acceptance/rejection."
    ),
    policies = c(nrow(freq_fit), nrow(freq_valid), nrow(freq_holdout)),
    claim_rows = c(nrow(sev_fit), nrow(sev_valid), nrow(sev_holdout)),
    row.names = NULL
  )

  c(
    gbm_results,
    list(
      gbm_results = gbm_results,
      gbm_learning_summary = gbm_learning_summary(gbm_results),
      validation_design = validation_design,
      enhanced_models = enhanced_final_models,
      enhanced_formulas = enhanced_formulas,
      term_decisions = term_decisions,
      synthesis_checks = synthesis_checks,
      validation_frequency_comparison = validation_frequency,
      validation_severity_comparison = validation_severity,
      validation_pure_premium_comparison = validation_pure_premium,
      synthesis_frequency_comparison = three_way_frequency,
      synthesis_severity_comparison = three_way_severity,
      synthesis_pure_premium_comparison = three_way_pure_premium,
      validation_calibrated_frequency_comparison = validation_calibrated_frequency,
      validation_calibrated_severity_comparison = validation_calibrated_severity,
      validation_calibrated_pure_premium_comparison = validation_calibrated_pure_premium,
      calibrated_frequency_comparison = holdout_calibrated_frequency,
      calibrated_severity_comparison = holdout_calibrated_severity,
      calibrated_pure_premium_comparison = holdout_calibrated_pure_premium,
      calibration_factors = calibration_factors,
      isotonic_status = isotonic_status,
      blend_grid = blend_selection$grid,
      selected_blend = blend_selection$selected,
      validation_candidate_metrics = validation_candidate_metrics,
      holdout_candidate_metrics = holdout_candidate_metrics,
      candidate_acceptance = candidate_acceptance,
      final_recommendation = final_recommendation,
      synthesis_frequency_deciles = three_way_frequency_deciles,
      synthesis_pure_premium_deciles = three_way_pure_premium_deciles,
      raw_ae_deciles = raw_ae_deciles,
      high_risk_decile_summary = high_risk_summary,
      candidate_high_risk_decile_summary = candidate_high_risk_summary,
      synthesis_business_impact = business_impact,
      synthesis_holdout_predictions = freq_eval,
      synthesis_validation_predictions = freq_valid_eval,
      synthesis_severity_holdout_predictions = sev_eval,
      synthesis_severity_validation_predictions = sev_valid_eval
    )
  )
}

if (sys.nframe() == 0) {
  results <- run_mtpl_gbm_glm_synthesis()
  cat("\nGBM learning summary:\n")
  print(results$gbm_learning_summary)
  cat("\nValidation design:\n")
  print(results$validation_design)
  cat("\nTerm decisions:\n")
  print(results$term_decisions)
  cat("\nCalibration factors:\n")
  print(results$calibration_factors)
  cat("\nCandidate acceptance:\n")
  print(results$candidate_acceptance)
  cat("\nFinal recommendation:\n")
  print(results$final_recommendation)
}
