source("mtpl_glm_analysis.R")

results <- run_mtpl_analysis()

output_dir <- file.path(getwd(), "streamlit_data")
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

write_named_table <- function(df, name) {
  write.csv(df, file.path(output_dir, paste0(name, ".csv")), row.names = FALSE)
}

named_matrix_to_df <- function(x, row_name_col) {
  df <- data.frame(
    term = rownames(x),
    x,
    row.names = NULL,
    check.names = FALSE
  )
  names(df)[1] <- row_name_col
  df
}

example_policy_df <- data.frame(
  example = rownames(results$example_policies),
  results$example_policies,
  row.names = NULL,
  check.names = FALSE
)

pure_premium <- results$pure_premium

summary_metrics <- data.frame(
  metric = c(
    "mean_pure_premium",
    "mean_annual_frequency",
    "mean_severity",
    "pure_premium_q10",
    "pure_premium_q25",
    "pure_premium_q50",
    "pure_premium_q75",
    "pure_premium_q90",
    "pure_premium_q95"
  ),
  value = c(
    mean(pure_premium$pred_pure_premium),
    mean(pure_premium$pred_frequency_annual),
    mean(pure_premium$pred_severity),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.10)),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.25)),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.50)),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.75)),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.90)),
    as.numeric(quantile(pure_premium$pred_pure_premium, 0.95))
  ),
  row.names = NULL
)

low_premium <- example_policy_df$pred_pure_premium[example_policy_df$example == "Lower-risk example"]
high_premium <- example_policy_df$pred_pure_premium[example_policy_df$example == "Higher-risk example"]
typical_premium <- example_policy_df$pred_pure_premium[example_policy_df$example == "Typical example"]

young_premium <- results$age_summary$pred_pure_premium[results$age_summary$DriverAgeBand == "[17,25]"]
old_premium <- results$age_summary$pred_pure_premium[results$age_summary$DriverAgeBand == "(70,Inf]"]

diesel_premium <- results$gas_summary$pred_pure_premium[results$gas_summary$Gas == "Diesel"]
regular_premium <- results$gas_summary$pred_pure_premium[results$gas_summary$Gas == "Regular"]

practical_comparisons <- data.frame(
  comparison = c(
    "Higher-risk vs lower-risk example",
    "Typical vs lower-risk example",
    "Age 17-25 vs age 70+",
    "Diesel vs Regular"
  ),
  ratio = c(
    high_premium / low_premium,
    typical_premium / low_premium,
    young_premium / old_premium,
    diesel_premium / regular_premium
  ),
  row.names = NULL
)

flags_df <- data.frame(
  flag = names(results$flags),
  value = unlist(results$flags),
  row.names = NULL
)

write_named_table(results$checks, "checks")
write_named_table(flags_df, "flags")
write_named_table(results$holdout_summary, "holdout_summary")
write_named_table(results$gas_summary, "gas_summary")
write_named_table(results$age_summary, "age_summary")
write_named_table(example_policy_df, "example_policies")
write_named_table(named_matrix_to_df(results$top_frequency_effects_quasi, "term"), "top_frequency_effects_quasi")
write_named_table(named_matrix_to_df(results$top_severity_effects, "term"), "top_severity_effects_raw")
write_named_table(named_matrix_to_df(results$top_severity_effects_capped, "term"), "top_severity_effects_capped")
write_named_table(results$frequency_deciles, "frequency_deciles")
write_named_table(results$severity_deciles, "severity_deciles")
write_named_table(summary_metrics, "summary_metrics")
write_named_table(practical_comparisons, "practical_comparisons")

pure_premium_sample <- pure_premium[, c(
  "PolicyID", "Power", "CarAge", "DriverAge", "Brand", "Gas", "Region",
  "pred_frequency_annual", "pred_severity", "pred_pure_premium"
)]

ordered_indices <- unique(pmax(1, round(c(0.10, 0.25, 0.50, 0.75, 0.90, 0.95) * nrow(pure_premium_sample))))
write_named_table(pure_premium_sample[ordered_indices, ], "pure_premium_examples")

cat("Exported Streamlit data to", output_dir, "\n")
