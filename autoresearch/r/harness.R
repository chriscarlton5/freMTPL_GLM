project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

source("mtpl_gbm_glm_synthesis.R")

`%||%` <- function(x, y) {
  if (is.null(x)) y else x
}

as_flag <- function(x, default = FALSE) {
  if (is.null(x)) {
    return(default)
  }
  isTRUE(x)
}

as_character_vec <- function(x) {
  if (is.null(x) || length(x) == 0) {
    return(character())
  }
  as.character(unlist(x, use.names = FALSE))
}

row_as_list <- function(df) {
  row <- as.list(df[1, , drop = TRUE])
  names(row) <- names(df)
  row
}

mean_or_na <- function(x) {
  x <- x[is.finite(x)]
  if (length(x) == 0) NA_real_ else mean(x)
}

sd_or_na <- function(x) {
  x <- x[is.finite(x)]
  if (length(x) <= 1) NA_real_ else stats::sd(x)
}

make_outer_folds <- function(flag, k = 3, seed = 20260423) {
  set.seed(seed)
  folds <- integer(length(flag))
  for (level in sort(unique(flag))) {
    idx <- which(flag == level)
    idx <- sample(idx)
    folds[idx] <- rep(seq_len(k), length.out = length(idx))
  }
  folds
}

prepare_research_data <- function(data_dir = ".", seed = 20260423, outer_folds = 3) {
  data <- load_gbm_model_data(data_dir = data_dir, seed = seed)
  severity_cap <- as.numeric(stats::quantile(data$sev_train$ClaimAmount, probs = 0.995, type = 7))

  freq_train <- add_capped_loss_columns(data$freq_train, data$sev, severity_cap)
  freq_holdout <- add_capped_loss_columns(data$freq_holdout, data$sev, severity_cap)
  sev_train <- data$sev_train
  sev_holdout <- data$sev_holdout
  sev_train$ClaimAmountCapped <- pmin(sev_train$ClaimAmount, severity_cap)
  sev_holdout$ClaimAmountCapped <- pmin(sev_holdout$ClaimAmount, severity_cap)

  freq_sets <- add_gbm_guided_feature_sets(
    reference_df = freq_train,
    datasets = list(train = freq_train, holdout = freq_holdout)
  )
  sev_sets <- add_gbm_guided_feature_sets(
    reference_df = sev_train,
    datasets = list(train = sev_train, holdout = sev_holdout)
  )
  freq_train <- freq_sets$train
  freq_holdout <- freq_sets$holdout
  sev_train <- sev_sets$train
  sev_holdout <- sev_sets$holdout

  freq_train$LogExposure <- log(freq_train$Exposure)
  freq_holdout$LogExposure <- log(freq_holdout$Exposure)

  freq_train$outer_fold <- make_outer_folds(
    as.integer(freq_train$ClaimNb > 0),
    k = outer_folds,
    seed = seed + 900
  )
  fold_lookup <- freq_train[, c("PolicyID", "outer_fold")]
  sev_train$outer_fold <- fold_lookup$outer_fold[match(sev_train$PolicyID, fold_lookup$PolicyID)]

  list(
    freq_train = freq_train,
    freq_holdout = freq_holdout,
    sev_train = sev_train,
    sev_holdout = sev_holdout,
    severity_cap = severity_cap,
    raw_counts = data$raw_counts,
    sev_all = data$sev
  )
}

candidate_component <- function(candidate, component_name) {
  candidate[[component_name]] %||% list()
}

fit_glm_models <- function(freq_fit, sev_fit, candidate) {
  freq_component <- candidate_component(candidate, "frequency")
  sev_component <- candidate_component(candidate, "severity")
  capped_component <- candidate_component(candidate, "capped_severity")

  list(
    frequency = fit_selected_model(
      train_df = freq_fit,
      response = "ClaimNb",
      family = poisson(link = "log"),
      use_splines = as_flag(freq_component$use_splines),
      interactions = as_character_vec(freq_component$interactions),
      offset_col = "LogExposure"
    ),
    severity = fit_selected_model(
      train_df = sev_fit,
      response = "ClaimAmount",
      family = Gamma(link = "log"),
      use_splines = as_flag(sev_component$use_splines),
      interactions = as_character_vec(sev_component$interactions)
    ),
    capped_severity = fit_selected_model(
      train_df = sev_fit,
      response = "ClaimAmountCapped",
      family = Gamma(link = "log"),
      use_splines = as_flag(capped_component$use_splines),
      interactions = as_character_vec(capped_component$interactions)
    )
  )
}

glm_predictions <- function(models, freq_valid, sev_valid) {
  freq_claims <- safe_response_prediction(models$frequency, freq_valid)
  freq_annual <- freq_claims / freq_valid$Exposure
  raw_sev_claim <- safe_response_prediction(models$severity, sev_valid)
  capped_sev_claim <- safe_response_prediction(models$capped_severity, sev_valid)
  raw_sev_policy <- safe_response_prediction(models$severity, freq_valid)
  capped_sev_policy <- safe_response_prediction(models$capped_severity, freq_valid)

  list(
    freq_claims = freq_claims,
    freq_annual = freq_annual,
    raw_severity_claim = raw_sev_claim,
    capped_severity_claim = capped_sev_claim,
    raw_severity_policy = raw_sev_policy,
    capped_severity_policy = capped_sev_policy
  )
}

component_scalars <- function(models, freq_cal, sev_cal) {
  preds <- glm_predictions(models, freq_cal, sev_cal)
  list(
    frequency = safe_ratio(sum(freq_cal$ClaimNb), sum(preds$freq_claims)),
    raw_severity = safe_ratio(mean(sev_cal$ClaimAmount), mean(preds$raw_severity_claim)),
    capped_severity = safe_ratio(mean(sev_cal$ClaimAmountCapped), mean(preds$capped_severity_claim))
  )
}

apply_scalars <- function(preds, scalars) {
  preds$freq_claims <- preds$freq_claims * scalars$frequency
  preds$freq_annual <- preds$freq_annual * scalars$frequency
  preds$raw_severity_claim <- preds$raw_severity_claim * scalars$raw_severity
  preds$raw_severity_policy <- preds$raw_severity_policy * scalars$raw_severity
  preds$capped_severity_claim <- preds$capped_severity_claim * scalars$capped_severity
  preds$capped_severity_policy <- preds$capped_severity_policy * scalars$capped_severity
  preds
}

default_frequency_grid <- function() {
  list(
    list(num_leaves = 15, min_data_in_leaf = 1000, learning_rate = 0.05, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 31, min_data_in_leaf = 1000, learning_rate = 0.03, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1)
  )
}

default_severity_grid <- function() {
  list(
    list(num_leaves = 7, min_data_in_leaf = 100, learning_rate = 0.05, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 15, min_data_in_leaf = 100, learning_rate = 0.03, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1)
  )
}

grid_from_candidate <- function(candidate, key, fallback) {
  lightgbm_spec <- candidate$lightgbm %||% list()
  grid <- lightgbm_spec[[key]]
  if (is.null(grid) || length(grid) == 0) {
    return(fallback())
  }
  grid
}

fit_lightgbm_models <- function(freq_fit, sev_fit, candidate, seed, fold) {
  lightgbm_spec <- candidate$lightgbm %||% list()
  nrounds <- as.integer(lightgbm_spec$nrounds %||% 150)
  early_stopping_rounds <- as.integer(lightgbm_spec$early_stopping_rounds %||% 20)

  fit_flag <- stratified_split(
    as.integer(freq_fit$ClaimNb > 0),
    train_fraction = 0.8,
    seed = seed + 1000 + fold
  )
  freq_fit$inner_split <- ifelse(fit_flag, "fit", "valid")
  lookup <- freq_fit[, c("PolicyID", "inner_split")]
  sev_fit$inner_split <- lookup$inner_split[match(sev_fit$PolicyID, lookup$PolicyID)]

  freq_inner_fit <- freq_fit[freq_fit$inner_split == "fit", ]
  freq_inner_valid <- freq_fit[freq_fit$inner_split == "valid", ]
  sev_inner_fit <- sev_fit[sev_fit$inner_split == "fit", ]
  sev_inner_valid <- sev_fit[sev_fit$inner_split == "valid", ]
  freq_inner_fit$frequency_target <- freq_inner_fit$ClaimNb / freq_inner_fit$Exposure
  freq_inner_valid$frequency_target <- freq_inner_valid$ClaimNb / freq_inner_valid$Exposure

  frequency_gbm <- train_lgb_grid(
    train_df = freq_inner_fit,
    valid_df = freq_inner_valid,
    label = "frequency_target",
    weight = "Exposure",
    objective = "poisson",
    metric_name = "poisson",
    grid = grid_from_candidate(candidate, "frequency_grid", default_frequency_grid),
    seed = seed + fold,
    nrounds = nrounds,
    early_stopping_rounds = early_stopping_rounds
  )
  severity_gbm <- train_lgb_grid(
    train_df = sev_inner_fit,
    valid_df = sev_inner_valid,
    label = "ClaimAmount",
    weight = NULL,
    objective = "gamma",
    metric_name = "gamma",
    grid = grid_from_candidate(candidate, "severity_grid", default_severity_grid),
    seed = seed + 100 + fold,
    nrounds = nrounds,
    early_stopping_rounds = early_stopping_rounds
  )
  capped_gbm <- train_lgb_grid(
    train_df = sev_inner_fit,
    valid_df = sev_inner_valid,
    label = "ClaimAmountCapped",
    weight = NULL,
    objective = "gamma",
    metric_name = "gamma",
    grid = grid_from_candidate(candidate, "capped_severity_grid", default_severity_grid),
    seed = seed + 200 + fold,
    nrounds = nrounds,
    early_stopping_rounds = early_stopping_rounds
  )

  list(
    frequency = frequency_gbm$model,
    severity = severity_gbm$model,
    capped_severity = capped_gbm$model,
    tuning = list(
      frequency = frequency_gbm$tuning,
      severity = severity_gbm$tuning,
      capped_severity = capped_gbm$tuning
    )
  )
}

lightgbm_predictions <- function(models, freq_valid, sev_valid) {
  freq_annual <- pmax(predict(models$frequency, encode_features(freq_valid)), 1e-12)
  raw_sev_claim <- pmax(predict(models$severity, encode_features(sev_valid)), 1e-12)
  capped_sev_claim <- pmax(predict(models$capped_severity, encode_features(sev_valid)), 1e-12)
  raw_sev_policy <- pmax(predict(models$severity, encode_features(freq_valid)), 1e-12)
  capped_sev_policy <- pmax(predict(models$capped_severity, encode_features(freq_valid)), 1e-12)
  list(
    freq_claims = freq_annual * freq_valid$Exposure,
    freq_annual = freq_annual,
    raw_severity_claim = raw_sev_claim,
    capped_severity_claim = capped_sev_claim,
    raw_severity_policy = raw_sev_policy,
    capped_severity_policy = capped_sev_policy
  )
}

evaluate_predictions <- function(freq_valid, sev_valid, preds, fold, diagnostics) {
  raw_pp <- preds$freq_annual * preds$raw_severity_policy
  capped_pp <- preds$freq_annual * preds$capped_severity_policy
  actual_frequency <- freq_valid$ClaimNb / freq_valid$Exposure
  raw_observed_loss_cost <- sum(freq_valid$ObservedLoss) / sum(freq_valid$Exposure)
  raw_predicted_loss_cost <- sum(raw_pp * freq_valid$Exposure) / sum(freq_valid$Exposure)
  capped_observed_loss_cost <- sum(freq_valid$ObservedLossCapped) / sum(freq_valid$Exposure)
  capped_predicted_loss_cost <- sum(capped_pp * freq_valid$Exposure) / sum(freq_valid$Exposure)

  data.frame(
    fold = fold,
    policies = nrow(freq_valid),
    claim_rows = nrow(sev_valid),
    observed_claims = sum(freq_valid$ClaimNb),
    predicted_claims = sum(preds$freq_claims),
    frequency_gini = ordered_lorenz_gini(freq_valid$ClaimNb, preds$freq_annual, freq_valid$Exposure),
    frequency_mae = weighted_mae(actual_frequency, preds$freq_annual, freq_valid$Exposure),
    frequency_rmse = weighted_rmse(actual_frequency, preds$freq_annual, freq_valid$Exposure),
    frequency_poisson_deviance = poisson_deviance(freq_valid$ClaimNb, preds$freq_claims),
    raw_severity_mae = mean(abs(sev_valid$ClaimAmount - preds$raw_severity_claim)),
    raw_severity_rmse = sqrt(mean((sev_valid$ClaimAmount - preds$raw_severity_claim)^2)),
    raw_severity_gamma_deviance = gamma_deviance(sev_valid$ClaimAmount, preds$raw_severity_claim),
    capped_severity_mae = mean(abs(sev_valid$ClaimAmountCapped - preds$capped_severity_claim)),
    capped_severity_rmse = sqrt(mean((sev_valid$ClaimAmountCapped - preds$capped_severity_claim)^2)),
    capped_severity_gamma_deviance = gamma_deviance(sev_valid$ClaimAmountCapped, preds$capped_severity_claim),
    raw_pp_gini = ordered_lorenz_gini(freq_valid$ObservedLoss, raw_pp, freq_valid$Exposure),
    raw_pp_mae = weighted_mae(freq_valid$ObservedLossAnnual, raw_pp, freq_valid$Exposure),
    raw_pp_rmse = weighted_rmse(freq_valid$ObservedLossAnnual, raw_pp, freq_valid$Exposure),
    raw_pp_observed_loss_cost = raw_observed_loss_cost,
    raw_pp_predicted_loss_cost = raw_predicted_loss_cost,
    raw_pp_calibration_gap = (raw_predicted_loss_cost - raw_observed_loss_cost) / raw_observed_loss_cost,
    capped_pp_gini = ordered_lorenz_gini(freq_valid$ObservedLossCapped, capped_pp, freq_valid$Exposure),
    capped_pp_mae = weighted_mae(freq_valid$ObservedLossCappedAnnual, capped_pp, freq_valid$Exposure),
    capped_pp_rmse = weighted_rmse(freq_valid$ObservedLossCappedAnnual, capped_pp, freq_valid$Exposure),
    capped_pp_observed_loss_cost = capped_observed_loss_cost,
    capped_pp_predicted_loss_cost = capped_predicted_loss_cost,
    capped_pp_calibration_gap = (capped_predicted_loss_cost - capped_observed_loss_cost) / capped_observed_loss_cost,
    bad_prediction_count = sum(!is.finite(unlist(preds))) + sum(unlist(preds) < 0, na.rm = TRUE),
    parameter_count = diagnostics$parameter_count,
    frequency_aic = diagnostics$frequency_aic,
    severity_aic = diagnostics$severity_aic,
    capped_severity_aic = diagnostics$capped_severity_aic,
    frequency_bic = diagnostics$frequency_bic,
    severity_bic = diagnostics$severity_bic,
    capped_severity_bic = diagnostics$capped_severity_bic,
    max_abs_coefficient = diagnostics$max_abs_coefficient,
    stringsAsFactors = FALSE
  )
}

model_diagnostics <- function(models, model_type) {
  if (model_type == "glm") {
    coefficients <- c(
      stats::coef(models$frequency),
      stats::coef(models$severity),
      stats::coef(models$capped_severity)
    )
    return(list(
      parameter_count = length(coefficients),
      frequency_aic = AIC(models$frequency),
      severity_aic = AIC(models$severity),
      capped_severity_aic = AIC(models$capped_severity),
      frequency_bic = BIC(models$frequency),
      severity_bic = BIC(models$severity),
      capped_severity_bic = BIC(models$capped_severity),
      max_abs_coefficient = max(abs(coefficients), na.rm = TRUE)
    ))
  }
  list(
    parameter_count = NA_real_,
    frequency_aic = NA_real_,
    severity_aic = NA_real_,
    capped_severity_aic = NA_real_,
    frequency_bic = NA_real_,
    severity_bic = NA_real_,
    capped_severity_bic = NA_real_,
    max_abs_coefficient = NA_real_
  )
}

evaluate_fold <- function(data, candidate, fold, seed) {
  freq_fit <- data$freq_train[data$freq_train$outer_fold != fold, ]
  freq_valid <- data$freq_train[data$freq_train$outer_fold == fold, ]
  sev_fit <- data$sev_train[data$sev_train$outer_fold != fold, ]
  sev_valid <- data$sev_train[data$sev_train$outer_fold == fold, ]
  model_type <- candidate$model_type %||% "glm"

  if (model_type == "lightgbm") {
    models <- fit_lightgbm_models(freq_fit, sev_fit, candidate, seed, fold)
    preds <- lightgbm_predictions(models, freq_valid, sev_valid)
    diagnostics <- model_diagnostics(models, model_type)
  } else {
    use_calibration <- as_flag((candidate$calibration %||% list())$component_scalars)
    if (use_calibration) {
      fit_flag <- stratified_split(
        as.integer(freq_fit$ClaimNb > 0),
        train_fraction = 0.8,
        seed = seed + 2000 + fold
      )
      freq_fit$inner_split <- ifelse(fit_flag, "fit", "calibration")
      lookup <- freq_fit[, c("PolicyID", "inner_split")]
      sev_fit$inner_split <- lookup$inner_split[match(sev_fit$PolicyID, lookup$PolicyID)]
      model_freq_fit <- freq_fit[freq_fit$inner_split == "fit", ]
      model_sev_fit <- sev_fit[sev_fit$inner_split == "fit", ]
      freq_cal <- freq_fit[freq_fit$inner_split == "calibration", ]
      sev_cal <- sev_fit[sev_fit$inner_split == "calibration", ]
      models <- fit_glm_models(model_freq_fit, model_sev_fit, candidate)
      scalars <- component_scalars(models, freq_cal, sev_cal)
      preds <- apply_scalars(glm_predictions(models, freq_valid, sev_valid), scalars)
    } else {
      models <- fit_glm_models(freq_fit, sev_fit, candidate)
      preds <- glm_predictions(models, freq_valid, sev_valid)
    }
    diagnostics <- model_diagnostics(models, model_type)
  }

  leakage <- length(intersect(freq_fit$PolicyID, freq_valid$PolicyID))
  metrics <- evaluate_predictions(freq_valid, sev_valid, preds, fold, diagnostics)
  metrics$policy_leakage_count <- leakage
  metrics
}

aggregate_metrics <- function(fold_metrics) {
  numeric_cols <- names(fold_metrics)[vapply(fold_metrics, is.numeric, logical(1))]
  out <- list()
  for (column in numeric_cols) {
    out[[paste0(column, "_mean")]] <- mean_or_na(fold_metrics[[column]])
    out[[paste0(column, "_sd")]] <- sd_or_na(fold_metrics[[column]])
  }
  out
}

fold_metrics_records <- function(fold_metrics) {
  lapply(seq_len(nrow(fold_metrics)), function(i) row_as_list(fold_metrics[i, , drop = FALSE]))
}

evaluate_candidate <- function(candidate) {
  seed <- as.integer(candidate$seed %||% 20260423)
  outer_folds <- as.integer(candidate$outer_folds %||% 3)
  data <- prepare_research_data(seed = seed, outer_folds = outer_folds)
  fold_rows <- lapply(seq_len(outer_folds), function(fold) {
    evaluate_fold(data, candidate, fold = fold, seed = seed)
  })
  fold_metrics <- do.call(rbind, fold_rows)
  aggregate <- aggregate_metrics(fold_metrics)

  observed_loss_reconciliation_gap <- sum(data$freq_train$ObservedLoss) +
    sum(data$freq_holdout$ObservedLoss) -
    sum(data$sev_all$ClaimAmount)

  metrics <- list(
    candidate_id = candidate$id %||% "candidate",
    candidate = candidate,
    model_type = candidate$model_type %||% "glm",
    outer_folds = outer_folds,
    seed = seed,
    severity_cap = data$severity_cap,
    aggregate = aggregate,
    fold_metrics = fold_metrics_records(fold_metrics),
    integrity = list(
      policy_leakage_count = sum(fold_metrics$policy_leakage_count, na.rm = TRUE),
      bad_prediction_count = sum(fold_metrics$bad_prediction_count, na.rm = TRUE),
      loss_reconciliation_gap = observed_loss_reconciliation_gap
    ),
    diagnostics = list(
      raw_counts = data$raw_counts
    )
  )

  list(metrics = metrics, fold_metrics = fold_metrics)
}
