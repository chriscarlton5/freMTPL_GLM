args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop(
    "Usage: robustness_runner.R <output_dir> <repo_root>",
    call. = FALSE
  )
}

output_dir <- args[[1]]
repo_root <- args[[2]]

setwd(repo_root)

project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required for robustness reporting.", call. = FALSE)
}

source(file.path("autoresearch", "r", "harness.R"))

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

read_candidate <- function(path) {
  jsonlite::fromJSON(path, simplifyVector = FALSE)
}

candidate_specs <- list(
  baseline_enhanced_glm_splines = read_candidate(file.path("autoresearch", "baselines", "baseline_metrics.json"))$candidate,
  lightgbm_regularized_challenger = read_candidate(file.path(
    "autoresearch",
    "evidence",
    "runs",
    "20260427_185953_5a72560_lightgbm_regularized_challenger",
    "candidate.json"
  )),
  lightgbm_best_191 = read_candidate(file.path(
    "autoresearch",
    "evidence",
    "runs",
    "20260428_174753_59f5be1_lightgbm_best_191",
    "candidate.json"
  ))
)

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
  metrics$model_type <- candidate$model_type %||% "glm"
  metrics$seed <- seed
  metrics
}

prediction_frame <- function(data, candidate, seed, policy_ids = NULL) {
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
  if (!is.null(policy_ids)) {
    out <- out[out$PolicyID %in% policy_ids, ]
  }
  out
}

importance_frame <- function(data, candidate, seed) {
  models <- fit_candidate_models(data, candidate, seed)
  if (!requireNamespace("lightgbm", quietly = TRUE)) {
    stop("Package 'lightgbm' is required for LightGBM importance stability.", call. = FALSE)
  }

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
      top_feature <- names(sort(table(unlist(top_sets)), decreasing = TRUE))[1]
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
        most_common_top_feature = top_feature,
        status = status,
        row.names = NULL
      )
    }
  }
  do.call(rbind, pieces)
}

format_num <- function(x, digits = 4) {
  ifelse(is.finite(x), formatC(x, format = "f", digits = digits), "NA")
}

write_markdown_summary <- function(path, holdout_metrics, seed_summary, prediction_summary, importance_summary) {
  best_row <- holdout_metrics[holdout_metrics$model_id == "lightgbm_best_191", ]
  initial_row <- holdout_metrics[holdout_metrics$model_id == "lightgbm_regularized_challenger", ]
  baseline_row <- holdout_metrics[holdout_metrics$model_id == "baseline_enhanced_glm_splines", ]

  best_validated <- nrow(best_row) == 1 &&
    nrow(initial_row) == 1 &&
    nrow(baseline_row) == 1 &&
    best_row$capped_pp_gini > initial_row$capped_pp_gini &&
    best_row$capped_pp_gini > baseline_row$capped_pp_gini &&
    abs(best_row$capped_pp_calibration_gap) <= 0.03 &&
    best_row$capped_pp_mae <= initial_row$capped_pp_mae * 1.01

  recommendation <- if (best_validated) {
    "Holdout validation supports keeping `lightgbm_best_191` as the current research pricing challenger, subject to the seed and interpretability stability review below."
  } else {
    "Holdout validation does not fully support promoting `lightgbm_best_191`; keep it as an autoresearch signal and favor the initial LightGBM or GLM for defensibility."
  }

  holdout_lines <- c(
    "| Model | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |",
    "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"
  )
  for (i in seq_len(nrow(holdout_metrics))) {
    row <- holdout_metrics[i, ]
    holdout_lines <- c(holdout_lines, paste0(
      "| `", row$model_id, "` | ",
      format_num(row$capped_pp_gini), " | ",
      format_num(row$raw_pp_gini), " | ",
      format_num(row$capped_pp_mae), " | ",
      format_num(row$capped_pp_calibration_gap), " | ",
      row$bad_prediction_count, " | ",
      row$policy_leakage_count, " |"
    ))
  }

  seed_lines <- c(
    "| Model | Metric | Mean | SD | Min | Max | Worst Delta |",
    "| --- | --- | ---: | ---: | ---: | ---: | ---: |"
  )
  for (i in seq_len(nrow(seed_summary))) {
    row <- seed_summary[i, ]
    seed_lines <- c(seed_lines, paste0(
      "| `", row$model_id, "` | `", row$metric, "` | ",
      format_num(row$mean), " | ",
      format_num(row$sd), " | ",
      format_num(row$min), " | ",
      format_num(row$max), " | ",
      format_num(row$worst_abs_delta_from_mean), " |"
    ))
  }

  prediction_lines <- c(
    "| Model | Prediction | Sampled Policies | Median CV | P95 CV | Max CV |",
    "| --- | --- | ---: | ---: | ---: | ---: |"
  )
  for (i in seq_len(nrow(prediction_summary))) {
    row <- prediction_summary[i, ]
    prediction_lines <- c(prediction_lines, paste0(
      "| `", row$model_id, "` | `", row$prediction, "` | ",
      row$sampled_policies, " | ",
      format_num(row$median_cv), " | ",
      format_num(row$p95_cv), " | ",
      format_num(row$max_cv), " |"
    ))
  }

  importance_lines <- c(
    "| Model | Component | Mean Top-5 Jaccard | Most Common Top Feature | Status |",
    "| --- | --- | ---: | --- | --- |"
  )
  for (i in seq_len(nrow(importance_summary))) {
    row <- importance_summary[i, ]
    importance_lines <- c(importance_lines, paste0(
      "| `", row$model_id, "` | `", row$component, "` | ",
      format_num(row$mean_top5_jaccard), " | `",
      row$most_common_top_feature, "` | ",
      row$status, " |"
    ))
  }

  text <- c(
    "# Robustness Validation Report",
    "",
    "This report is a locked post-selection validation layer. It does not update autoresearch champions, gates, or historical run evidence.",
    "",
    "## Recommendation",
    "",
    recommendation,
    "",
    "## Blind Holdout Metrics",
    "",
    holdout_lines,
    "",
    "## Seed Metric Stability",
    "",
    seed_lines,
    "",
    "## Policy Prediction Stability",
    "",
    prediction_lines,
    "",
    "## Interpretability Stability",
    "",
    importance_lines,
    "",
    "## Governance Note",
    "",
    "`lightgbm_best_191` remains a CV-selected autoresearch champion unless this holdout and stability evidence is reviewed by a human model owner. Python generated candidate specs and launched runs; R remains the metric, split, and modeling source of truth."
  )
  writeLines(text, path, useBytes = TRUE)
}

base_seed <- 20260423
stability_seeds <- c(20260423, 20260431, 20260439, 20260447, 20260455)
data <- prepare_research_data(seed = base_seed, outer_folds = 3)

holdout_metrics <- do.call(rbind, lapply(candidate_specs, function(candidate) {
  holdout_metrics_for_candidate(data, candidate, seed = base_seed)
}))
holdout_metrics <- holdout_metrics[, c(
  "model_id", "model_type", "policies", "claim_rows", "observed_claims", "predicted_claims",
  "frequency_gini", "frequency_mae", "frequency_rmse", "frequency_poisson_deviance",
  "raw_pp_gini", "raw_pp_mae", "raw_pp_rmse", "raw_pp_observed_loss_cost",
  "raw_pp_predicted_loss_cost", "raw_pp_calibration_gap",
  "capped_pp_gini", "capped_pp_mae", "capped_pp_rmse", "capped_pp_observed_loss_cost",
  "capped_pp_predicted_loss_cost", "capped_pp_calibration_gap",
  "bad_prediction_count", "policy_leakage_count"
)]

lightgbm_candidates <- candidate_specs[c("lightgbm_regularized_challenger", "lightgbm_best_191")]

seed_metric_rows <- list()
sample_policy_ids <- sort(sample(data$freq_holdout$PolicyID, size = min(1000, nrow(data$freq_holdout))))
prediction_rows <- list()
importance_rows <- list()

for (candidate in lightgbm_candidates) {
  for (seed in stability_seeds) {
    seed_metric_rows[[length(seed_metric_rows) + 1]] <- holdout_metrics_for_candidate(data, candidate, seed = seed)
    prediction_rows[[length(prediction_rows) + 1]] <- prediction_frame(data, candidate, seed, sample_policy_ids)
    importance_rows[[length(importance_rows) + 1]] <- importance_frame(data, candidate, seed)
  }
}

seed_metrics <- do.call(rbind, seed_metric_rows)
seed_metrics <- seed_metrics[, c(
  "model_id", "seed", "capped_pp_gini", "raw_pp_gini", "capped_pp_mae", "capped_pp_rmse",
  "capped_pp_calibration_gap", "raw_pp_calibration_gap", "bad_prediction_count", "policy_leakage_count"
)]
prediction_stability <- do.call(rbind, prediction_rows)
importance_stability <- do.call(rbind, importance_rows)

seed_summary <- metric_summary(
  seed_metrics,
  c("capped_pp_gini", "raw_pp_gini", "capped_pp_mae", "capped_pp_calibration_gap")
)
prediction_summary <- prediction_stability_summary(prediction_stability)
importance_summary <- importance_stability_summary(importance_stability)

write.csv(holdout_metrics, file.path(output_dir, "holdout_metrics.csv"), row.names = FALSE, na = "")
write.csv(seed_metrics, file.path(output_dir, "seed_metrics.csv"), row.names = FALSE, na = "")
write.csv(seed_summary, file.path(output_dir, "seed_summary.csv"), row.names = FALSE, na = "")
write.csv(prediction_summary, file.path(output_dir, "prediction_stability_summary.csv"), row.names = FALSE, na = "")
write.csv(importance_stability, file.path(output_dir, "feature_importance_by_seed.csv"), row.names = FALSE, na = "")
write.csv(importance_summary, file.path(output_dir, "feature_importance_summary.csv"), row.names = FALSE, na = "")

payload <- list(
  generated_at = as.character(Sys.time()),
  base_seed = base_seed,
  stability_seeds = stability_seeds,
  holdout_metrics = holdout_metrics,
  seed_summary = seed_summary,
  prediction_stability_summary = prediction_summary,
  feature_importance_summary = importance_summary
)
jsonlite::write_json(
  payload,
  file.path(output_dir, "robustness_summary.json"),
  pretty = TRUE,
  auto_unbox = TRUE,
  null = "null",
  na = "null"
)

write_markdown_summary(
  file.path(output_dir, "robustness_report.md"),
  holdout_metrics,
  seed_summary,
  prediction_summary,
  importance_summary
)
