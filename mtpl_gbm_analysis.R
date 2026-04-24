project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

source("mtpl_glm_analysis.R")

required_gbm_package <- function() {
  if (!requireNamespace("lightgbm", quietly = TRUE)) {
    stop(
      "Package 'lightgbm' is required. Install it with install.packages('lightgbm').",
      call. = FALSE
    )
  }
}

weighted_mean <- function(x, w) {
  sum(w * x, na.rm = TRUE) / sum(w, na.rm = TRUE)
}

weighted_mae <- function(actual, predicted, w = rep(1, length(actual))) {
  weighted_mean(abs(actual - predicted), w)
}

weighted_rmse <- function(actual, predicted, w = rep(1, length(actual))) {
  sqrt(weighted_mean((actual - predicted)^2, w))
}

poisson_deviance <- function(actual, predicted, w = rep(1, length(actual))) {
  predicted <- pmax(predicted, 1e-12)
  term <- ifelse(actual == 0, 0, actual * log(pmax(actual, 1e-12) / predicted)) - (actual - predicted)
  2 * sum(w * term, na.rm = TRUE) / sum(w, na.rm = TRUE)
}

gamma_deviance <- function(actual, predicted, w = rep(1, length(actual))) {
  predicted <- pmax(predicted, 1e-12)
  actual <- pmax(actual, 1e-12)
  term <- (actual - predicted) / predicted - log(actual / predicted)
  2 * sum(w * term, na.rm = TRUE) / sum(w, na.rm = TRUE)
}

ordered_lorenz_gini <- function(actual, score, exposure = rep(1, length(actual))) {
  valid <- is.finite(actual) & is.finite(score) & is.finite(exposure) & exposure > 0
  actual <- actual[valid]
  score <- score[valid]
  exposure <- exposure[valid]
  if (length(actual) == 0 || sum(actual) <= 0 || sum(exposure) <= 0) {
    return(NA_real_)
  }

  ordered <- order(score, decreasing = TRUE)
  exposure_share <- c(0, cumsum(exposure[ordered]) / sum(exposure))
  actual_share <- c(0, cumsum(actual[ordered]) / sum(actual))
  area <- sum(diff(exposure_share) * (head(actual_share, -1) + tail(actual_share, -1)) / 2)
  2 * area - 1
}

encode_features <- function(df) {
  feature_cols <- c("Power", "CarAge", "DriverAge", "Brand", "Gas", "Region", "logDensity")
  categorical_cols <- c("Power", "Brand", "Gas", "Region")

  encoded <- data.frame(row.names = seq_len(nrow(df)))
  for (column in feature_cols) {
    if (column %in% categorical_cols) {
      encoded[[column]] <- as.integer(df[[column]]) - 1
    } else {
      encoded[[column]] <- as.numeric(df[[column]])
    }
  }
  as.matrix(encoded[, feature_cols, drop = FALSE])
}

load_gbm_model_data <- function(data_dir = ".", seed = 20260423) {
  freq_path <- file.path(data_dir, "freMTPLfreq.csv")
  sev_path <- file.path(data_dir, "freMTPLsev.csv")

  freq <- read.csv(freq_path, stringsAsFactors = FALSE)
  sev <- read.csv(sev_path, stringsAsFactors = FALSE)

  raw_counts <- list(freq_rows = nrow(freq), sev_rows = nrow(sev))

  freq <- freq[complete.cases(freq[, c(
    "PolicyID", "ClaimNb", "Exposure", "Power", "CarAge",
    "DriverAge", "Brand", "Gas", "Region", "Density"
  )]), ]
  freq <- freq[freq$Exposure > 0, ]
  freq$logDensity <- log1p(freq$Density)
  freq <- prepare_factor_columns(freq)

  train_flag <- stratified_split(as.integer(freq$ClaimNb > 0), seed = seed)
  freq$split <- ifelse(train_flag, "train", "holdout")
  freq <- ensure_training_levels(freq, "split", c("Power", "Brand", "Gas", "Region"))

  sev <- sev[complete.cases(sev[, c("PolicyID", "ClaimAmount")]), ]
  sev <- sev[sev$ClaimAmount > 0, ]

  loss_by_policy <- aggregate(ClaimAmount ~ PolicyID, data = sev, FUN = sum)
  names(loss_by_policy)[2] <- "ObservedLoss"
  freq$ObservedLoss <- loss_by_policy$ObservedLoss[match(freq$PolicyID, loss_by_policy$PolicyID)]
  freq$ObservedLoss[is.na(freq$ObservedLoss)] <- 0
  freq$ObservedLossAnnual <- freq$ObservedLoss / freq$Exposure

  severity_columns <- c(
    "PolicyID", "split", "Power", "CarAge", "DriverAge", "Brand", "Gas", "Region", "Density", "logDensity"
  )
  sev_model_data <- merge(
    sev,
    freq[, severity_columns],
    by = "PolicyID",
    all.x = FALSE,
    all.y = FALSE,
    sort = FALSE
  )

  freq_train <- freq[freq$split == "train", ]
  freq_holdout <- freq[freq$split == "holdout", ]

  fit_flag <- stratified_split(as.integer(freq_train$ClaimNb > 0), train_fraction = 0.8, seed = seed + 1)
  freq_train$gbm_split <- ifelse(fit_flag, "fit", "valid")

  sev_train <- sev_model_data[sev_model_data$split == "train", ]
  sev_holdout <- sev_model_data[sev_model_data$split == "holdout", ]
  split_lookup <- freq_train[, c("PolicyID", "gbm_split")]
  sev_train <- merge(sev_train, split_lookup, by = "PolicyID", all.x = TRUE, sort = FALSE)

  list(
    raw_counts = raw_counts,
    freq = freq,
    sev = sev,
    freq_train = freq_train,
    freq_holdout = freq_holdout,
    sev_train = sev_train,
    sev_holdout = sev_holdout
  )
}

add_capped_loss_columns <- function(freq_df, sev_df, severity_cap) {
  sev_capped <- sev_df[, c("PolicyID", "ClaimAmount")]
  sev_capped$ClaimAmountCapped <- pmin(sev_capped$ClaimAmount, severity_cap)
  capped_by_policy <- aggregate(ClaimAmountCapped ~ PolicyID, data = sev_capped, FUN = sum)
  names(capped_by_policy)[2] <- "ObservedLossCapped"

  freq_df$ObservedLossCapped <- capped_by_policy$ObservedLossCapped[
    match(freq_df$PolicyID, capped_by_policy$PolicyID)
  ]
  freq_df$ObservedLossCapped[is.na(freq_df$ObservedLossCapped)] <- 0
  freq_df$ObservedLossCappedAnnual <- freq_df$ObservedLossCapped / freq_df$Exposure
  freq_df
}

train_lgb_grid <- function(train_df, valid_df, label, weight, objective, metric_name,
                           grid, seed, nrounds = 350, early_stopping_rounds = 25) {
  required_gbm_package()

  categorical_cols <- c("Power", "Brand", "Gas", "Region")
  x_train <- encode_features(train_df)
  x_valid <- encode_features(valid_df)
  y_train <- train_df[[label]]
  y_valid <- valid_df[[label]]
  w_train <- if (is.null(weight)) rep(1, nrow(train_df)) else train_df[[weight]]
  w_valid <- if (is.null(weight)) rep(1, nrow(valid_df)) else valid_df[[weight]]

  dtrain <- lightgbm::lgb.Dataset(
    data = x_train,
    label = y_train,
    weight = w_train,
    categorical_feature = categorical_cols,
    free_raw_data = FALSE
  )
  dvalid <- lightgbm::lgb.Dataset(
    data = x_valid,
    label = y_valid,
    weight = w_valid,
    categorical_feature = categorical_cols,
    free_raw_data = FALSE
  )

  best_model <- NULL
  best_score <- Inf
  tuning_rows <- list()

  for (i in seq_along(grid)) {
    params <- c(
      list(
        objective = objective,
        metric = metric_name,
        seed = seed + i,
        num_threads = 2,
        verbosity = -1,
        force_col_wise = TRUE,
        feature_pre_filter = FALSE,
        bagging_freq = 1
      ),
      grid[[i]]
    )

    model <- lightgbm::lgb.train(
      params = params,
      data = dtrain,
      nrounds = nrounds,
      valids = list(valid = dvalid),
      early_stopping_rounds = early_stopping_rounds,
      verbose = -1
    )

    valid_pred <- predict(model, x_valid)
    valid_pred <- pmax(valid_pred, 1e-12)
    score <- if (objective == "poisson") {
      poisson_deviance(y_valid, valid_pred, w_valid)
    } else {
      gamma_deviance(y_valid, valid_pred, w_valid)
    }

    best_iter <- model$best_iter
    if (is.null(best_iter) || length(best_iter) == 0) {
      best_iter <- nrounds
    }

    tuning_rows[[i]] <- data.frame(
      candidate = i,
      objective = objective,
      validation_deviance = score,
      best_iter = best_iter,
      num_leaves = params$num_leaves,
      min_data_in_leaf = params$min_data_in_leaf,
      learning_rate = params$learning_rate,
      feature_fraction = params$feature_fraction,
      bagging_fraction = params$bagging_fraction,
      lambda_l2 = params$lambda_l2,
      row.names = NULL
    )

    if (score < best_score) {
      best_score <- score
      best_model <- model
    }
  }

  list(
    model = best_model,
    tuning = do.call(rbind, tuning_rows),
    validation_score = best_score
  )
}

frequency_metrics <- function(df) {
  actual_frequency <- df$ClaimNb / df$Exposure
  data.frame(
    model = c("GLM", "LightGBM"),
    observed_claims = sum(df$ClaimNb),
    predicted_claims = c(sum(df$glm_pred_claims), sum(df$gbm_pred_claims)),
    observed_annual_frequency = sum(df$ClaimNb) / sum(df$Exposure),
    predicted_annual_frequency = c(
      sum(df$glm_pred_claims) / sum(df$Exposure),
      sum(df$gbm_pred_claims) / sum(df$Exposure)
    ),
    weighted_mae_annual_frequency = c(
      weighted_mae(actual_frequency, df$glm_pred_frequency_annual, df$Exposure),
      weighted_mae(actual_frequency, df$gbm_pred_frequency_annual, df$Exposure)
    ),
    weighted_rmse_annual_frequency = c(
      weighted_rmse(actual_frequency, df$glm_pred_frequency_annual, df$Exposure),
      weighted_rmse(actual_frequency, df$gbm_pred_frequency_annual, df$Exposure)
    ),
    pricing_lift_gini = c(
      ordered_lorenz_gini(df$ClaimNb, df$glm_pred_frequency_annual, df$Exposure),
      ordered_lorenz_gini(df$ClaimNb, df$gbm_pred_frequency_annual, df$Exposure)
    ),
    row.names = NULL
  )
}

severity_metrics <- function(df, actual_col, glm_pred_col, gbm_pred_col, label) {
  data.frame(
    target = label,
    model = c("GLM", "LightGBM"),
    observed_mean = mean(df[[actual_col]]),
    predicted_mean = c(mean(df[[glm_pred_col]]), mean(df[[gbm_pred_col]])),
    mae = c(
      mean(abs(df[[actual_col]] - df[[glm_pred_col]])),
      mean(abs(df[[actual_col]] - df[[gbm_pred_col]]))
    ),
    rmse = c(
      sqrt(mean((df[[actual_col]] - df[[glm_pred_col]])^2)),
      sqrt(mean((df[[actual_col]] - df[[gbm_pred_col]])^2))
    ),
    row.names = NULL
  )
}

pure_premium_metrics <- function(df, glm_pp_col, gbm_pp_col, label,
                                 observed_loss_col = "ObservedLoss",
                                 observed_loss_annual_col = "ObservedLossAnnual") {
  observed_loss <- df[[observed_loss_col]]
  observed_loss_annual <- df[[observed_loss_annual_col]]
  data.frame(
    target = label,
    model = c("GLM", "LightGBM"),
    observed_total_loss = sum(observed_loss),
    predicted_total_loss = c(
      sum(df[[glm_pp_col]] * df$Exposure),
      sum(df[[gbm_pp_col]] * df$Exposure)
    ),
    observed_loss_cost = sum(observed_loss) / sum(df$Exposure),
    predicted_loss_cost = c(
      sum(df[[glm_pp_col]] * df$Exposure) / sum(df$Exposure),
      sum(df[[gbm_pp_col]] * df$Exposure) / sum(df$Exposure)
    ),
    weighted_mae_annual_loss_cost = c(
      weighted_mae(observed_loss_annual, df[[glm_pp_col]], df$Exposure),
      weighted_mae(observed_loss_annual, df[[gbm_pp_col]], df$Exposure)
    ),
    weighted_rmse_annual_loss_cost = c(
      weighted_rmse(observed_loss_annual, df[[glm_pp_col]], df$Exposure),
      weighted_rmse(observed_loss_annual, df[[gbm_pp_col]], df$Exposure)
    ),
    pricing_lift_gini = c(
      ordered_lorenz_gini(observed_loss, df[[glm_pp_col]], df$Exposure),
      ordered_lorenz_gini(observed_loss, df[[gbm_pp_col]], df$Exposure)
    ),
    row.names = NULL
  )
}

frequency_deciles <- function(df, score_col, claim_col, model_name) {
  decile <- safe_quantile_groups(df[[score_col]])
  observed <- tapply(df$ClaimNb, decile, sum)
  predicted <- tapply(df[[claim_col]], decile, sum)
  exposure <- tapply(df$Exposure, decile, sum)
  data.frame(
    model = model_name,
    decile = seq_along(observed),
    observed_annual_frequency = as.numeric(observed / exposure),
    predicted_annual_frequency = as.numeric(predicted / exposure),
    exposure = as.numeric(exposure),
    row.names = NULL
  )
}

severity_deciles <- function(df, score_col, actual_col, pred_col, model_name, target_name) {
  decile <- safe_quantile_groups(df[[score_col]])
  observed <- tapply(df[[actual_col]], decile, mean)
  predicted <- tapply(df[[pred_col]], decile, mean)
  claims <- tapply(df[[actual_col]], decile, length)
  data.frame(
    target = target_name,
    model = model_name,
    decile = seq_along(observed),
    observed_mean = as.numeric(observed),
    predicted_mean = as.numeric(predicted),
    claims = as.integer(claims),
    row.names = NULL
  )
}

pure_premium_deciles <- function(df, score_col, pp_col, model_name, target_name,
                                 observed_loss_col = "ObservedLoss") {
  decile <- safe_quantile_groups(df[[score_col]])
  observed_loss <- tapply(df[[observed_loss_col]], decile, sum)
  predicted_loss <- tapply(df[[pp_col]] * df$Exposure, decile, sum)
  exposure <- tapply(df$Exposure, decile, sum)
  data.frame(
    target = target_name,
    model = model_name,
    decile = seq_along(observed_loss),
    observed_loss_cost = as.numeric(observed_loss / exposure),
    predicted_loss_cost = as.numeric(predicted_loss / exposure),
    exposure = as.numeric(exposure),
    row.names = NULL
  )
}

importance_or_empty <- function(model) {
  out <- lightgbm::lgb.importance(model, percentage = TRUE)
  if (is.null(out) || nrow(out) == 0) {
    return(data.frame(Feature = character(), Gain = numeric(), Cover = numeric(), Frequency = numeric()))
  }
  out
}

select_importance_features <- function(importance, fallback, count = 3) {
  features <- unique(c(as.character(head(importance$Feature, count)), fallback))
  features[features %in% c("Power", "CarAge", "DriverAge", "Brand", "Gas", "Region", "logDensity")]
}

partial_dependence <- function(model, base_df, feature, model_name, target_name, max_rows = 5000) {
  set.seed(20260423)
  if (nrow(base_df) > max_rows) {
    base_df <- base_df[sample(seq_len(nrow(base_df)), max_rows), ]
  }

  categorical_cols <- c("Power", "Brand", "Gas", "Region")
  if (feature %in% categorical_cols) {
    counts <- sort(table(base_df[[feature]]), decreasing = TRUE)
    labels <- names(head(counts, 10))
    values <- seq_along(labels) - 1
  } else {
    values <- unique(as.numeric(quantile(base_df[[feature]], probs = seq(0.05, 0.95, length.out = 12), na.rm = TRUE)))
    labels <- format(round(values, 3), trim = TRUE)
  }

  rows <- vector("list", length(values))
  for (i in seq_along(values)) {
    x <- encode_features(base_df)
    x[, feature] <- values[i]
    rows[[i]] <- data.frame(
      target = target_name,
      model = model_name,
      feature = feature,
      value = labels[i],
      mean_prediction = mean(predict(model, x)),
      row.names = NULL
    )
  }
  do.call(rbind, rows)
}

interaction_summary <- function(df, row_group, col_group, label, max_rows = 16) {
  aggregate_df <- aggregate(
    cbind(ObservedLoss, Exposure, glm_loss = glm_pred_loss, gbm_loss = gbm_pred_loss) ~
      df[[row_group]] + df[[col_group]],
    data = df,
    FUN = sum
  )
  names(aggregate_df)[1:2] <- c(row_group, col_group)
  aggregate_df$observed_loss_cost <- aggregate_df$ObservedLoss / aggregate_df$Exposure
  aggregate_df$glm_predicted_loss_cost <- aggregate_df$glm_loss / aggregate_df$Exposure
  aggregate_df$gbm_predicted_loss_cost <- aggregate_df$gbm_loss / aggregate_df$Exposure
  aggregate_df$interaction <- label
  aggregate_df <- aggregate_df[order(aggregate_df$Exposure, decreasing = TRUE), ]
  head(aggregate_df[, c(
    "interaction", row_group, col_group, "Exposure",
    "observed_loss_cost", "glm_predicted_loss_cost", "gbm_predicted_loss_cost"
  )], max_rows)
}

build_interaction_tables <- function(freq_holdout) {
  df <- freq_holdout
  df$DriverAgeBand <- cut(df$DriverAge, breaks = c(17, 25, 35, 50, 70, Inf), include.lowest = TRUE)
  df$CarAgeBand <- cut(df$CarAge, breaks = c(-Inf, 1, 5, 10, 20, Inf), include.lowest = TRUE)
  df$DensityBand <- cut(df$logDensity, breaks = unique(quantile(df$logDensity, seq(0, 1, 0.25))), include.lowest = TRUE)
  df$glm_pred_loss <- df$glm_pred_pure_premium * df$Exposure
  df$gbm_pred_loss <- df$gbm_pred_pure_premium * df$Exposure

  region_exposure <- sort(tapply(df$Exposure, df$Region, sum), decreasing = TRUE)
  top_regions <- names(head(region_exposure, 6))
  region_df <- df[df$Region %in% top_regions, ]

  list(
    driver_car_age = interaction_summary(df, "DriverAgeBand", "CarAgeBand", "DriverAge x CarAge"),
    power_brand = interaction_summary(df, "Power", "Brand", "Power x Brand"),
    region_density = interaction_summary(region_df, "Region", "DensityBand", "Region x logDensity")
  )
}

run_mtpl_gbm_analysis <- function(data_dir = ".", seed = 20260423) {
  required_gbm_package()

  glm_results <- run_mtpl_analysis(data_dir = data_dir, seed = seed)
  data <- load_gbm_model_data(data_dir = data_dir, seed = seed)

  freq_train <- data$freq_train
  freq_holdout <- data$freq_holdout
  sev_train <- data$sev_train
  sev_holdout <- data$sev_holdout

  severity_cap <- glm_results$severity_cap
  data$freq <- add_capped_loss_columns(data$freq, data$sev, severity_cap)
  freq_train <- add_capped_loss_columns(freq_train, data$sev, severity_cap)
  freq_holdout <- add_capped_loss_columns(freq_holdout, data$sev, severity_cap)

  sev_train$ClaimAmountCapped <- pmin(sev_train$ClaimAmount, severity_cap)
  sev_holdout$ClaimAmountCapped <- pmin(sev_holdout$ClaimAmount, severity_cap)

  freq_fit <- freq_train[freq_train$gbm_split == "fit", ]
  freq_valid <- freq_train[freq_train$gbm_split == "valid", ]
  sev_fit <- sev_train[sev_train$gbm_split == "fit", ]
  sev_valid <- sev_train[sev_train$gbm_split == "valid", ]

  frequency_grid <- list(
    list(num_leaves = 15, min_data_in_leaf = 1000, learning_rate = 0.05, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 31, min_data_in_leaf = 1000, learning_rate = 0.03, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 31, min_data_in_leaf = 500, learning_rate = 0.05, feature_fraction = 0.8, bagging_fraction = 0.8, lambda_l2 = 5),
    list(num_leaves = 15, min_data_in_leaf = 500, learning_rate = 0.08, feature_fraction = 0.8, bagging_fraction = 0.9, lambda_l2 = 3)
  )

  severity_grid <- list(
    list(num_leaves = 7, min_data_in_leaf = 100, learning_rate = 0.05, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 15, min_data_in_leaf = 100, learning_rate = 0.03, feature_fraction = 0.9, bagging_fraction = 0.9, lambda_l2 = 1),
    list(num_leaves = 15, min_data_in_leaf = 50, learning_rate = 0.05, feature_fraction = 0.8, bagging_fraction = 0.8, lambda_l2 = 5),
    list(num_leaves = 31, min_data_in_leaf = 100, learning_rate = 0.03, feature_fraction = 0.8, bagging_fraction = 0.9, lambda_l2 = 5)
  )

  freq_fit$frequency_target <- freq_fit$ClaimNb / freq_fit$Exposure
  freq_valid$frequency_target <- freq_valid$ClaimNb / freq_valid$Exposure

  frequency_gbm <- train_lgb_grid(
    train_df = freq_fit,
    valid_df = freq_valid,
    label = "frequency_target",
    weight = "Exposure",
    objective = "poisson",
    metric_name = "poisson",
    grid = frequency_grid,
    seed = seed
  )

  severity_gbm <- train_lgb_grid(
    train_df = sev_fit,
    valid_df = sev_valid,
    label = "ClaimAmount",
    weight = NULL,
    objective = "gamma",
    metric_name = "gamma",
    grid = severity_grid,
    seed = seed + 100
  )

  capped_severity_gbm <- train_lgb_grid(
    train_df = sev_fit,
    valid_df = sev_valid,
    label = "ClaimAmountCapped",
    weight = NULL,
    objective = "gamma",
    metric_name = "gamma",
    grid = severity_grid,
    seed = seed + 200
  )

  freq_holdout$glm_pred_claims <- predict(glm_results$freq_fit, newdata = freq_holdout, type = "response")
  freq_holdout$glm_pred_frequency_annual <- freq_holdout$glm_pred_claims / freq_holdout$Exposure
  freq_holdout$gbm_pred_frequency_annual <- pmax(predict(frequency_gbm$model, encode_features(freq_holdout)), 0)
  freq_holdout$gbm_pred_claims <- freq_holdout$gbm_pred_frequency_annual * freq_holdout$Exposure

  sev_holdout$glm_pred_severity <- predict(glm_results$sev_fit, newdata = sev_holdout, type = "response")
  sev_holdout$glm_pred_severity_capped <- predict(glm_results$sev_capped_fit, newdata = sev_holdout, type = "response")
  sev_holdout$gbm_pred_severity <- pmax(predict(severity_gbm$model, encode_features(sev_holdout)), 0)
  sev_holdout$gbm_pred_severity_capped <- pmax(predict(capped_severity_gbm$model, encode_features(sev_holdout)), 0)

  freq_holdout$glm_pred_severity <- predict(glm_results$sev_fit, newdata = freq_holdout, type = "response")
  freq_holdout$glm_pred_severity_capped <- predict(glm_results$sev_capped_fit, newdata = freq_holdout, type = "response")
  freq_holdout$gbm_pred_severity <- pmax(predict(severity_gbm$model, encode_features(freq_holdout)), 0)
  freq_holdout$gbm_pred_severity_capped <- pmax(predict(capped_severity_gbm$model, encode_features(freq_holdout)), 0)

  freq_holdout$glm_pred_pure_premium <- freq_holdout$glm_pred_frequency_annual * freq_holdout$glm_pred_severity
  freq_holdout$gbm_pred_pure_premium <- freq_holdout$gbm_pred_frequency_annual * freq_holdout$gbm_pred_severity
  freq_holdout$glm_pred_pure_premium_capped <- freq_holdout$glm_pred_frequency_annual * freq_holdout$glm_pred_severity_capped
  freq_holdout$gbm_pred_pure_premium_capped <- freq_holdout$gbm_pred_frequency_annual * freq_holdout$gbm_pred_severity_capped

  freq_holdout$glm_pred_loss <- freq_holdout$glm_pred_pure_premium * freq_holdout$Exposure
  freq_holdout$gbm_pred_loss <- freq_holdout$gbm_pred_pure_premium * freq_holdout$Exposure

  frequency_comparison <- frequency_metrics(freq_holdout)
  severity_comparison <- rbind(
    severity_metrics(sev_holdout, "ClaimAmount", "glm_pred_severity", "gbm_pred_severity", "Raw severity"),
    severity_metrics(sev_holdout, "ClaimAmountCapped", "glm_pred_severity_capped", "gbm_pred_severity_capped", "Capped severity")
  )
  pure_premium_comparison <- rbind(
    pure_premium_metrics(freq_holdout, "glm_pred_pure_premium", "gbm_pred_pure_premium", "Raw severity pure premium"),
    pure_premium_metrics(
      freq_holdout,
      "glm_pred_pure_premium_capped",
      "gbm_pred_pure_premium_capped",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped",
      observed_loss_annual_col = "ObservedLossCappedAnnual"
    )
  )

  frequency_decile_summary <- rbind(
    frequency_deciles(freq_holdout, "glm_pred_frequency_annual", "glm_pred_claims", "GLM"),
    frequency_deciles(freq_holdout, "gbm_pred_frequency_annual", "gbm_pred_claims", "LightGBM")
  )

  severity_decile_summary <- rbind(
    severity_deciles(sev_holdout, "glm_pred_severity", "ClaimAmount", "glm_pred_severity", "GLM", "Raw severity"),
    severity_deciles(sev_holdout, "gbm_pred_severity", "ClaimAmount", "gbm_pred_severity", "LightGBM", "Raw severity"),
    severity_deciles(sev_holdout, "glm_pred_severity_capped", "ClaimAmountCapped", "glm_pred_severity_capped", "GLM", "Capped severity"),
    severity_deciles(sev_holdout, "gbm_pred_severity_capped", "ClaimAmountCapped", "gbm_pred_severity_capped", "LightGBM", "Capped severity")
  )

  pure_premium_decile_summary <- rbind(
    pure_premium_deciles(freq_holdout, "glm_pred_pure_premium", "glm_pred_pure_premium", "GLM", "Raw severity pure premium"),
    pure_premium_deciles(freq_holdout, "gbm_pred_pure_premium", "gbm_pred_pure_premium", "LightGBM", "Raw severity pure premium"),
    pure_premium_deciles(
      freq_holdout,
      "glm_pred_pure_premium_capped",
      "glm_pred_pure_premium_capped",
      "GLM",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped"
    ),
    pure_premium_deciles(
      freq_holdout,
      "gbm_pred_pure_premium_capped",
      "gbm_pred_pure_premium_capped",
      "LightGBM",
      "Capped severity pure premium",
      observed_loss_col = "ObservedLossCapped"
    )
  )

  importance <- list(
    frequency = importance_or_empty(frequency_gbm$model),
    severity = importance_or_empty(severity_gbm$model),
    capped_severity = importance_or_empty(capped_severity_gbm$model)
  )

  pdp_features_frequency <- select_importance_features(importance$frequency, c("DriverAge", "CarAge", "logDensity"), count = 3)
  pdp_features_severity <- select_importance_features(importance$capped_severity, c("DriverAge", "CarAge", "logDensity"), count = 3)

  pdp_frequency <- do.call(rbind, lapply(
    unique(pdp_features_frequency),
    function(feature) partial_dependence(frequency_gbm$model, freq_holdout, feature, "LightGBM", "Annual frequency")
  ))
  pdp_severity <- do.call(rbind, lapply(
    unique(pdp_features_severity),
    function(feature) partial_dependence(capped_severity_gbm$model, freq_holdout, feature, "LightGBM", "Capped severity")
  ))

  interaction_tables <- build_interaction_tables(freq_holdout)

  checks <- data.frame(
    metric = c(
      "policy_rows_raw",
      "policy_rows_after_cleaning",
      "claim_rows_raw",
      "claim_rows_after_cleaning",
      "train_policies",
      "holdout_policies",
      "train_claim_rows",
      "holdout_claim_rows",
      "gbm_fit_policies",
      "gbm_validation_policies",
      "gbm_fit_claim_rows",
      "gbm_validation_claim_rows",
      "train_holdout_policy_leakage",
      "gbm_fit_validation_policy_leakage",
      "observed_loss_reconciliation_gap",
      "capped_observed_loss_reconciliation_gap",
      "severity_cap_99_5"
    ),
    value = c(
      data$raw_counts$freq_rows,
      nrow(data$freq),
      data$raw_counts$sev_rows,
      nrow(data$sev),
      nrow(freq_train),
      nrow(freq_holdout),
      nrow(sev_train),
      nrow(sev_holdout),
      nrow(freq_fit),
      nrow(freq_valid),
      nrow(sev_fit),
      nrow(sev_valid),
      length(intersect(freq_train$PolicyID, freq_holdout$PolicyID)),
      length(intersect(freq_fit$PolicyID, freq_valid$PolicyID)),
      sum(data$freq$ObservedLoss) - sum(data$sev$ClaimAmount),
      sum(data$freq$ObservedLossCapped) - sum(pmin(data$sev$ClaimAmount, severity_cap)),
      severity_cap
    ),
    row.names = NULL
  )

  frequency_gini_delta <- frequency_comparison$pricing_lift_gini[frequency_comparison$model == "LightGBM"] -
    frequency_comparison$pricing_lift_gini[frequency_comparison$model == "GLM"]
  pure_gini_delta <- pure_premium_comparison$pricing_lift_gini[
    pure_premium_comparison$model == "LightGBM" &
      pure_premium_comparison$target == "Raw severity pure premium"
  ] - pure_premium_comparison$pricing_lift_gini[
    pure_premium_comparison$model == "GLM" &
      pure_premium_comparison$target == "Raw severity pure premium"
  ]

  model_value <- data.frame(
    question = c(
      "Did GBM rank frequency risk better?",
      "Did GBM rank pure premium risk better?",
      "Did GBM materially simplify the severity problem?",
      "What is the main use of GBM here?"
    ),
    answer = c(
      ifelse(is.finite(frequency_gini_delta) && frequency_gini_delta > 0.005, "Yes, frequency Gini improved meaningfully.", "No material frequency-ranking improvement over GLM."),
      ifelse(is.finite(pure_gini_delta) && pure_gini_delta > 0.005, "Yes, pure-premium Gini improved meaningfully.", "No material pure-premium ranking improvement over GLM."),
      "No. Severity remains tail-sensitive, so raw and capped views should both be shown.",
      "Use it as a challenger model and interaction-discovery tool, not as an automatic replacement for the GLM."
    ),
    row.names = NULL
  )

  list(
    checks = checks,
    glm_results = glm_results,
    frequency_comparison = frequency_comparison,
    severity_comparison = severity_comparison,
    pure_premium_comparison = pure_premium_comparison,
    frequency_deciles = frequency_decile_summary,
    severity_deciles = severity_decile_summary,
    pure_premium_deciles = pure_premium_decile_summary,
    tuning = list(
      frequency = frequency_gbm$tuning,
      severity = severity_gbm$tuning,
      capped_severity = capped_severity_gbm$tuning
    ),
    importance = importance,
    pdp = rbind(pdp_frequency, pdp_severity),
    interactions = interaction_tables,
    model_value = model_value,
    severity_cap = severity_cap,
    gbm_models = list(
      frequency = frequency_gbm$model,
      severity = severity_gbm$model,
      capped_severity = capped_severity_gbm$model
    ),
    holdout_predictions = freq_holdout,
    severity_holdout_predictions = sev_holdout
  )
}

if (sys.nframe() == 0) {
  results <- run_mtpl_gbm_analysis()
  cat("\nChecks:\n")
  print(results$checks)
  cat("\nFrequency comparison:\n")
  print(results$frequency_comparison)
  cat("\nSeverity comparison:\n")
  print(results$severity_comparison)
  cat("\nPure premium comparison:\n")
  print(results$pure_premium_comparison)
  cat("\nModel value:\n")
  print(results$model_value)
}
