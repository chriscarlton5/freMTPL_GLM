prepare_factor_columns <- function(df) {
  df$Power <- factor(df$Power)
  df$Brand <- factor(df$Brand)
  df$Gas <- factor(df$Gas)
  df$Region <- factor(df$Region)
  df
}

stratified_split <- function(flag, train_fraction = 0.8, seed = 20260423) {
  set.seed(seed)
  train_index <- rep(FALSE, length(flag))
  for (level in sort(unique(flag))) {
    level_index <- which(flag == level)
    n_train <- floor(length(level_index) * train_fraction)
    if (length(level_index) > 0 && n_train > 0) {
      train_index[sample(level_index, n_train)] <- TRUE
    }
  }
  train_index
}

ensure_training_levels <- function(df, split_name, factor_cols) {
  for (column in factor_cols) {
    holdout_values <- unique(as.character(df[df[[split_name]] == "holdout", column]))
    train_values <- unique(as.character(df[df[[split_name]] == "train", column]))
    missing_from_train <- setdiff(holdout_values, train_values)
    if (length(missing_from_train) > 0) {
      move_rows <- df[[split_name]] == "holdout" & as.character(df[[column]]) %in% missing_from_train
      df[[split_name]][move_rows] <- "train"
    }
  }
  df
}

safe_quantile_groups <- function(x, groups = 10) {
  probs <- seq(0, 1, length.out = groups + 1)
  breaks <- unique(as.numeric(quantile(x, probs = probs, na.rm = TRUE, type = 7)))
  if (length(breaks) < 2) {
    return(factor(rep("All", length(x))))
  }
  cut(x, breaks = breaks, include.lowest = TRUE, ordered_result = TRUE)
}

top_effects <- function(model_summary, count = 10) {
  coef_table <- model_summary$coefficients
  coef_table <- coef_table[rownames(coef_table) != "(Intercept)", , drop = FALSE]
  if (nrow(coef_table) == 0) {
    return(coef_table)
  }
  ordered <- order(abs(coef_table[, "Estimate"]), decreasing = TRUE)
  coef_table[head(ordered, count), , drop = FALSE]
}

decile_frequency_summary <- function(df) {
  decile <- safe_quantile_groups(df$pred_frequency_annual)
  observed <- tapply(df$ClaimNb, decile, sum)
  predicted <- tapply(df$pred_claims, decile, sum)
  exposure <- tapply(df$Exposure, decile, sum)
  data.frame(
    decile = names(observed),
    observed_frequency = as.numeric(observed / exposure),
    predicted_frequency = as.numeric(predicted / exposure),
    exposure = as.numeric(exposure),
    row.names = NULL
  )
}

decile_severity_summary <- function(df) {
  decile <- safe_quantile_groups(df$pred_claim_amount)
  observed <- tapply(df$ClaimAmount, decile, mean)
  predicted <- tapply(df$pred_claim_amount, decile, mean)
  counts <- tapply(df$ClaimAmount, decile, length)
  data.frame(
    decile = names(observed),
    observed_severity = as.numeric(observed),
    predicted_severity = as.numeric(predicted),
    claims = as.integer(counts),
    row.names = NULL
  )
}

holdout_summary_table <- function(freq_holdout, sev_holdout, freq_dispersion) {
  data.frame(
    metric = c(
      "Observed claims",
      "Predicted claims",
      "Observed annual frequency",
      "Predicted annual frequency",
      "Observed mean severity",
      "Predicted mean severity",
      "Observed capped mean severity",
      "Predicted capped mean severity",
      "Frequency dispersion"
    ),
    value = c(
      sum(freq_holdout$ClaimNb),
      sum(freq_holdout$pred_claims),
      sum(freq_holdout$ClaimNb) / sum(freq_holdout$Exposure),
      sum(freq_holdout$pred_claims) / sum(freq_holdout$Exposure),
      mean(sev_holdout$ClaimAmount),
      mean(sev_holdout$pred_claim_amount),
      mean(sev_holdout$ClaimAmountCapped),
      mean(sev_holdout$pred_claim_amount_capped),
      freq_dispersion
    ),
    row.names = NULL
  )
}

run_mtpl_analysis <- function(data_dir = ".", seed = 20260423) {
  freq_path <- file.path(data_dir, "freMTPLfreq.csv")
  sev_path <- file.path(data_dir, "freMTPLsev.csv")

  freq <- read.csv(freq_path, stringsAsFactors = FALSE)
  sev <- read.csv(sev_path, stringsAsFactors = FALSE)

  raw_counts <- list(
    freq_rows = nrow(freq),
    sev_rows = nrow(sev)
  )

  freq <- freq[complete.cases(freq[, c("PolicyID", "ClaimNb", "Exposure", "Power", "CarAge", "DriverAge", "Brand", "Gas", "Region", "Density")]), ]
  freq <- freq[freq$Exposure > 0, ]
  freq$logDensity <- log1p(freq$Density)
  freq <- prepare_factor_columns(freq)

  train_flag <- stratified_split(as.integer(freq$ClaimNb > 0), seed = seed)
  freq$split <- ifelse(train_flag, "train", "holdout")
  freq <- ensure_training_levels(freq, "split", c("Power", "Brand", "Gas", "Region"))

  sev <- sev[complete.cases(sev[, c("PolicyID", "ClaimAmount")]), ]
  sev <- sev[sev$ClaimAmount > 0, ]

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
  sev_train <- sev_model_data[sev_model_data$split == "train", ]
  sev_holdout <- sev_model_data[sev_model_data$split == "holdout", ]

  frequency_formula <- ClaimNb ~ Power + CarAge + DriverAge + Brand + Gas + Region + logDensity
  severity_formula <- ClaimAmount ~ Power + CarAge + DriverAge + Brand + Gas + Region + logDensity

  freq_fit <- glm(
    formula = frequency_formula,
    family = poisson(link = "log"),
    data = freq_train,
    offset = log(Exposure)
  )

  sev_fit <- glm(
    formula = severity_formula,
    family = Gamma(link = "log"),
    data = sev_train
  )

  freq_quasi_fit <- glm(
    formula = frequency_formula,
    family = quasipoisson(link = "log"),
    data = freq_train,
    offset = log(Exposure)
  )

  freq_train$pred_claims <- predict(freq_fit, newdata = freq_train, type = "response")
  freq_holdout$pred_claims <- predict(freq_fit, newdata = freq_holdout, type = "response")
  freq_train$pred_frequency_annual <- freq_train$pred_claims / freq_train$Exposure
  freq_holdout$pred_frequency_annual <- freq_holdout$pred_claims / freq_holdout$Exposure

  sev_train$pred_claim_amount <- predict(sev_fit, newdata = sev_train, type = "response")
  sev_holdout$pred_claim_amount <- predict(sev_fit, newdata = sev_holdout, type = "response")

  freq_dispersion <- sum(residuals(freq_fit, type = "pearson")^2) / freq_fit$df.residual

  severity_cap <- as.numeric(quantile(sev_train$ClaimAmount, probs = 0.995, type = 7))
  sev_train$ClaimAmountCapped <- pmin(sev_train$ClaimAmount, severity_cap)
  sev_holdout$ClaimAmountCapped <- pmin(sev_holdout$ClaimAmount, severity_cap)

  sev_capped_fit <- glm(
    formula = ClaimAmountCapped ~ Power + CarAge + DriverAge + Brand + Gas + Region + logDensity,
    family = Gamma(link = "log"),
    data = sev_train
  )

  sev_train$pred_claim_amount_capped <- predict(sev_capped_fit, newdata = sev_train, type = "response")
  sev_holdout$pred_claim_amount_capped <- predict(sev_capped_fit, newdata = sev_holdout, type = "response")

  annualized_policies <- freq
  annualized_policies$Exposure <- 1
  annualized_policies$pred_frequency_annual <- predict(freq_fit, newdata = annualized_policies, type = "response")
  annualized_policies$pred_severity <- predict(sev_fit, newdata = annualized_policies, type = "response")
  annualized_policies$pred_pure_premium <- annualized_policies$pred_frequency_annual * annualized_policies$pred_severity

  annualized_policies$DriverAgeBand <- cut(
    annualized_policies$DriverAge,
    breaks = c(17, 25, 35, 50, 70, Inf),
    include.lowest = TRUE,
    right = TRUE
  )

  annualized_policies$CarAgeBand <- cut(
    annualized_policies$CarAge,
    breaks = c(-Inf, 1, 5, 10, 20, Inf),
    include.lowest = TRUE,
    right = TRUE
  )

  gas_summary <- aggregate(
    annualized_policies[, c("pred_frequency_annual", "pred_severity", "pred_pure_premium")],
    by = list(Gas = annualized_policies$Gas),
    FUN = mean
  )

  age_summary <- aggregate(
    annualized_policies[, c("pred_frequency_annual", "pred_severity", "pred_pure_premium")],
    by = list(DriverAgeBand = annualized_policies$DriverAgeBand),
    FUN = mean
  )

  ordered_policies <- annualized_policies[order(annualized_policies$pred_pure_premium), ]
  example_index <- pmax(1, pmin(nrow(ordered_policies), round(c(0.10, 0.50, 0.90) * nrow(ordered_policies))))
  example_policies <- ordered_policies[example_index, c(
    "PolicyID", "Power", "CarAge", "DriverAge", "Brand", "Gas", "Region",
    "pred_frequency_annual", "pred_severity", "pred_pure_premium"
  )]
  rownames(example_policies) <- c("Lower-risk example", "Typical example", "Higher-risk example")

  freq_summary <- summary(freq_fit)
  freq_quasi_summary <- summary(freq_quasi_fit)
  sev_summary <- summary(sev_fit)
  sev_capped_summary <- summary(sev_capped_fit)
  sev_cooks <- cooks.distance(sev_fit)

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
      "holdout_observed_claims",
      "holdout_predicted_claims",
      "holdout_observed_annual_frequency",
      "holdout_predicted_annual_frequency",
      "holdout_observed_mean_severity",
      "holdout_predicted_mean_severity",
      "holdout_observed_capped_mean_severity",
      "holdout_predicted_capped_mean_severity",
      "severity_cap_99_5",
      "frequency_dispersion"
    ),
    value = c(
      raw_counts$freq_rows,
      nrow(freq),
      raw_counts$sev_rows,
      nrow(sev),
      nrow(freq_train),
      nrow(freq_holdout),
      nrow(sev_train),
      nrow(sev_holdout),
      sum(freq_holdout$ClaimNb),
      sum(freq_holdout$pred_claims),
      sum(freq_holdout$ClaimNb) / sum(freq_holdout$Exposure),
      sum(freq_holdout$pred_claims) / sum(freq_holdout$Exposure),
      mean(sev_holdout$ClaimAmount),
      mean(sev_holdout$pred_claim_amount),
      mean(sev_holdout$ClaimAmountCapped),
      mean(sev_holdout$pred_claim_amount_capped),
      severity_cap,
      freq_dispersion
    ),
    row.names = NULL
  )

  flags <- list(
    frequency_overdispersed = is.finite(freq_dispersion) && freq_dispersion > 1.5,
    severity_outlier_heavy = max(sev$ClaimAmount) > (20 * median(sev$ClaimAmount)),
    frequency_holdout_gap = abs(sum(freq_holdout$pred_claims) - sum(freq_holdout$ClaimNb)) / max(1, sum(freq_holdout$ClaimNb)) > 0.20,
    severity_holdout_gap = abs(mean(sev_holdout$pred_claim_amount) - mean(sev_holdout$ClaimAmount)) / mean(sev_holdout$ClaimAmount) > 0.20,
    capped_severity_holdout_gap = abs(mean(sev_holdout$pred_claim_amount_capped) - mean(sev_holdout$ClaimAmountCapped)) / mean(sev_holdout$ClaimAmountCapped) > 0.20
  )

  list(
    frequency_formula = deparse(frequency_formula),
    severity_formula = deparse(severity_formula),
    checks = checks,
    flags = flags,
    freq_fit = freq_fit,
    freq_quasi_fit = freq_quasi_fit,
    sev_fit = sev_fit,
    sev_capped_fit = sev_capped_fit,
    freq_summary = freq_summary,
    freq_quasi_summary = freq_quasi_summary,
    sev_summary = sev_summary,
    sev_capped_summary = sev_capped_summary,
    top_frequency_effects = top_effects(freq_summary, count = 10),
    top_frequency_effects_quasi = top_effects(freq_quasi_summary, count = 10),
    top_severity_effects = top_effects(sev_summary, count = 10),
    top_severity_effects_capped = top_effects(sev_capped_summary, count = 10),
    frequency_deciles = decile_frequency_summary(freq_holdout),
    severity_deciles = decile_severity_summary(sev_holdout),
    holdout_summary = holdout_summary_table(freq_holdout, sev_holdout, freq_dispersion),
    gas_summary = gas_summary,
    age_summary = age_summary,
    example_policies = example_policies,
    pure_premium = annualized_policies,
    severity_cooks_top = sort(sev_cooks, decreasing = TRUE)[1:10],
    severity_cap = severity_cap
  )
}

if (sys.nframe() == 0) {
  results <- run_mtpl_analysis()
  print(results$checks)
  cat("\nFlags:\n")
  print(results$flags)
}
