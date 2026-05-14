args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 4) {
  stop(
    "Usage: v2_runner.R <candidate.json> <benchmark.json> <output_dir> <repo_root> [seed_csv]",
    call. = FALSE
  )
}

candidate_path <- args[[1]]
benchmark_path <- args[[2]]
output_dir <- args[[3]]
repo_root <- args[[4]]
seed_csv <- if (length(args) >= 5) args[[5]] else "20260423,20260431,20260439"

setwd(repo_root)

project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required for v2 candidate parsing.", call. = FALSE)
}

source(file.path("autoresearch", "r", "harness.R"))

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

read_wrapper <- function(path) {
  jsonlite::fromJSON(path, simplifyVector = FALSE)
}

model_spec <- function(wrapper) {
  wrapper$model_spec %||% wrapper
}

fit_candidate_models <- function(data, candidate, seed) {
  if ((candidate$model_type %||% "glm") == "lightgbm") {
    return(fit_lightgbm_models(data$freq_train, data$sev_train, candidate, seed = seed, fold = 0))
  }
  fit_glm_models(data$freq_train, data$sev_train, candidate)
}

predict_candidate <- function(models, candidate, freq_df, sev_df) {
  if ((candidate$model_type %||% "glm") == "lightgbm") {
    return(lightgbm_predictions(models, freq_df, sev_df))
  }
  glm_predictions(models, freq_df, sev_df)
}

holdout_metrics_for_candidate <- function(data, candidate, seed) {
  models <- fit_candidate_models(data, candidate, seed)
  preds <- predict_candidate(models, candidate, data$freq_holdout, data$sev_holdout)
  diagnostics <- model_diagnostics(models, candidate$model_type %||% "glm")
  metrics <- evaluate_predictions(
    data$freq_holdout,
    data$sev_holdout,
    preds,
    fold = 0,
    diagnostics = diagnostics
  )
  metrics$policy_leakage_count <- length(intersect(data$freq_train$PolicyID, data$freq_holdout$PolicyID))
  metrics$model_id <- candidate$id
  metrics$seed <- seed
  metrics
}

prediction_frame <- function(data, candidate, seed, policy_ids) {
  models <- fit_candidate_models(data, candidate, seed)
  preds <- predict_candidate(models, candidate, data$freq_holdout, data$sev_holdout)
  capped_pp <- preds$freq_annual * preds$capped_severity_policy
  raw_pp <- preds$freq_annual * preds$raw_severity_policy
  out <- data.frame(
    model_id = candidate$id,
    seed = seed,
    PolicyID = data$freq_holdout$PolicyID,
    capped_pp = capped_pp,
    raw_pp = raw_pp,
    row.names = NULL
  )
  out[out$PolicyID %in% policy_ids, ]
}

importance_frame <- function(data, candidate, seed) {
  if ((candidate$model_type %||% "glm") != "lightgbm") {
    return(data.frame())
  }
  if (!requireNamespace("lightgbm", quietly = TRUE)) {
    stop("Package 'lightgbm' is required for LightGBM importance stability.", call. = FALSE)
  }
  models <- fit_candidate_models(data, candidate, seed)

  component_rows <- function(component_name, model) {
    importance <- lightgbm::lgb.importance(model)
    if (is.null(importance) || nrow(importance) == 0) {
      return(data.frame())
    }
    importance$model_id <- candidate$id
    importance$seed <- seed
    importance$component <- component_name
    importance$rank <- seq_len(nrow(importance))
    importance[, c("model_id", "seed", "component", "Feature", "Gain", "Cover", "Frequency", "rank")]
  }

  do.call(rbind, list(
    component_rows("frequency", models$frequency),
    component_rows("severity", models$severity),
    component_rows("capped_severity", models$capped_severity)
  ))
}

metric_summary <- function(rows, metric_cols) {
  pieces <- list()
  for (model_id in unique(rows$model_id)) {
    model_rows <- rows[rows$model_id == model_id, ]
    for (metric_col in metric_cols) {
      x <- model_rows[[metric_col]]
      pieces[[length(pieces) + 1]] <- data.frame(
        model_id = model_id,
        metric = metric_col,
        mean = mean(x, na.rm = TRUE),
        sd = stats::sd(x, na.rm = TRUE),
        min = min(x, na.rm = TRUE),
        max = max(x, na.rm = TRUE),
        worst_abs_delta_from_mean = max(abs(x - mean(x, na.rm = TRUE)), na.rm = TRUE),
        row.names = NULL
      )
    }
  }
  do.call(rbind, pieces)
}

prediction_stability_summary <- function(pred_rows) {
  pieces <- list()
  for (model_id in unique(pred_rows$model_id)) {
    model_rows <- pred_rows[pred_rows$model_id == model_id, ]
    for (metric_col in c("capped_pp", "raw_pp")) {
      by_policy <- aggregate(
        model_rows[[metric_col]],
        by = list(PolicyID = model_rows$PolicyID),
        FUN = function(x) {
          m <- mean(x, na.rm = TRUE)
          if (!is.finite(m) || abs(m) < 1e-12) {
            return(0)
          }
          stats::sd(x, na.rm = TRUE) / abs(m)
        }
      )
      names(by_policy)[2] <- "cv"
      pieces[[length(pieces) + 1]] <- data.frame(
        model_id = model_id,
        prediction = metric_col,
        sampled_policies = nrow(by_policy),
        median_cv = stats::median(by_policy$cv, na.rm = TRUE),
        p95_cv = as.numeric(stats::quantile(by_policy$cv, 0.95, na.rm = TRUE, type = 7)),
        max_cv = max(by_policy$cv, na.rm = TRUE),
        row.names = NULL
      )
    }
  }
  do.call(rbind, pieces)
}

importance_stability_summary <- function(importance_rows) {
  if (is.null(importance_rows) || nrow(importance_rows) == 0) {
    return(data.frame())
  }
  pieces <- list()
  for (model_id in unique(importance_rows$model_id)) {
    model_rows <- importance_rows[importance_rows$model_id == model_id, ]
    for (component in unique(model_rows$component)) {
      component_rows <- model_rows[model_rows$component == component, ]
      seeds <- sort(unique(component_rows$seed))
      top_sets <- lapply(seeds, function(seed) {
        seed_rows <- component_rows[component_rows$seed == seed, ]
        head(seed_rows$Feature[order(seed_rows$rank)], 5)
      })
      overlaps <- c()
      if (length(top_sets) > 1) {
        for (i in seq_len(length(top_sets) - 1)) {
          for (j in seq((i + 1), length(top_sets))) {
            union_size <- length(union(top_sets[[i]], top_sets[[j]]))
            overlaps <- c(overlaps, length(intersect(top_sets[[i]], top_sets[[j]])) / max(union_size, 1))
          }
        }
      }
      mean_overlap <- if (length(overlaps) == 0) NA_real_ else mean(overlaps)
      status <- if (is.na(mean_overlap)) {
        "needs_review"
      } else if (mean_overlap >= 0.7) {
        "stable"
      } else if (mean_overlap >= 0.5) {
        "needs_review"
      } else {
        "unstable"
      }
      pieces[[length(pieces) + 1]] <- data.frame(
        model_id = model_id,
        component = component,
        mean_top5_jaccard = mean_overlap,
        status = status,
        row.names = NULL
      )
    }
  }
  do.call(rbind, pieces)
}

candidate_wrapper <- read_wrapper(candidate_path)
benchmark_wrapper <- read_wrapper(benchmark_path)
candidate <- model_spec(candidate_wrapper)
benchmark <- model_spec(benchmark_wrapper)
stability_seeds <- as.integer(strsplit(seed_csv, ",", fixed = TRUE)[[1]])
base_seed <- stability_seeds[[1]]
data <- prepare_research_data(seed = base_seed, outer_folds = 3)

cv_result <- evaluate_candidate(candidate)
benchmark_holdout <- holdout_metrics_for_candidate(data, benchmark, seed = base_seed)
candidate_holdout <- holdout_metrics_for_candidate(data, candidate, seed = base_seed)

seed_metrics <- do.call(rbind, lapply(stability_seeds, function(seed) {
  holdout_metrics_for_candidate(data, candidate, seed = seed)
}))
seed_metrics <- seed_metrics[, c(
  "model_id", "seed", "capped_pp_gini", "raw_pp_gini", "capped_pp_mae",
  "capped_pp_rmse", "capped_pp_calibration_gap", "raw_pp_calibration_gap",
  "bad_prediction_count", "policy_leakage_count"
)]
seed_summary <- metric_summary(
  seed_metrics,
  c("capped_pp_gini", "raw_pp_gini", "capped_pp_mae", "capped_pp_calibration_gap")
)

sample_policy_ids <- sort(sample(data$freq_holdout$PolicyID, size = min(1000, nrow(data$freq_holdout))))
prediction_rows <- do.call(rbind, lapply(stability_seeds, function(seed) {
  prediction_frame(data, candidate, seed, sample_policy_ids)
}))
prediction_summary <- prediction_stability_summary(prediction_rows)

importance_rows <- do.call(rbind, lapply(stability_seeds, function(seed) {
  importance_frame(data, candidate, seed)
}))
importance_summary <- importance_stability_summary(importance_rows)

holdout_comparison <- rbind(
  transform(benchmark_holdout, role = "benchmark"),
  transform(candidate_holdout, role = "candidate")
)
holdout_comparison <- holdout_comparison[, c(
  "role", "model_id", "seed", "policies", "claim_rows", "observed_claims", "predicted_claims",
  "frequency_gini", "raw_pp_gini", "raw_pp_mae", "raw_pp_rmse",
  "raw_pp_observed_loss_cost", "raw_pp_predicted_loss_cost", "raw_pp_calibration_gap",
  "capped_pp_gini", "capped_pp_mae", "capped_pp_rmse",
  "capped_pp_observed_loss_cost", "capped_pp_predicted_loss_cost", "capped_pp_calibration_gap",
  "bad_prediction_count", "policy_leakage_count"
)]

write.csv(holdout_comparison, file.path(output_dir, "holdout_comparison.csv"), row.names = FALSE, na = "")
write.csv(cv_result$fold_metrics, file.path(output_dir, "cv_fold_metrics.csv"), row.names = FALSE, na = "")
write.csv(seed_metrics, file.path(output_dir, "seed_metrics.csv"), row.names = FALSE, na = "")
write.csv(seed_summary, file.path(output_dir, "seed_summary.csv"), row.names = FALSE, na = "")
write.csv(prediction_summary, file.path(output_dir, "prediction_stability_summary.csv"), row.names = FALSE, na = "")
write.csv(importance_rows, file.path(output_dir, "feature_importance_by_seed.csv"), row.names = FALSE, na = "")
write.csv(importance_summary, file.path(output_dir, "feature_importance_summary.csv"), row.names = FALSE, na = "")

payload <- list(
  candidate = candidate_wrapper,
  benchmark = benchmark_wrapper,
  cv_metrics = cv_result$metrics,
  holdout_comparison = holdout_comparison,
  seed_summary = seed_summary,
  prediction_stability_summary = prediction_summary,
  feature_importance_summary = importance_summary
)

jsonlite::write_json(
  payload,
  file.path(output_dir, "r_metrics.json"),
  pretty = TRUE,
  auto_unbox = TRUE,
  null = "null",
  na = "null"
)
