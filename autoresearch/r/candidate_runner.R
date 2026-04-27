args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 4) {
  stop(
    "Usage: candidate_runner.R <candidate.json> <metrics.json> <fold_metrics.csv> <repo_root>",
    call. = FALSE
  )
}

candidate_path <- args[[1]]
metrics_path <- args[[2]]
fold_metrics_path <- args[[3]]
repo_root <- args[[4]]

setwd(repo_root)

project_library <- file.path(getwd(), "r_libs")
if (dir.exists(project_library)) {
  .libPaths(c(project_library, .libPaths()))
}

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required for autoresearch candidate parsing.", call. = FALSE)
}

source(file.path("autoresearch", "r", "harness.R"))

candidate <- jsonlite::fromJSON(candidate_path, simplifyVector = FALSE)
result <- evaluate_candidate(candidate)

jsonlite::write_json(
  result$metrics,
  metrics_path,
  pretty = TRUE,
  auto_unbox = TRUE,
  null = "null",
  na = "null"
)
write.csv(result$fold_metrics, fold_metrics_path, row.names = FALSE, na = "")
