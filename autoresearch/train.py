from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0007",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.511 L2=13.1 L=16",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5108232624507447,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 13.091811728094841
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46082326245074473,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 11.091811728094841
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5108232624507447,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 11.091811728094841
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46082326245074473,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 10.091811728094841
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5108232624507447,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 11.091811728094841
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46082326245074473,
        "bagging_fraction": 0.5108232624507447,
        "lambda_l2": 10.091811728094841
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)