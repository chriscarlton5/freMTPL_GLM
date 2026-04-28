from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0006",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.519 L2=13.2 L=14",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 14,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5186112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 13.243535848170936
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4686112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 11.243535848170936
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5186112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 11.243535848170936
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4686112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 10.243535848170936
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5186112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 11.243535848170936
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4686112595681338,
        "bagging_fraction": 0.5186112595681338,
        "lambda_l2": 10.243535848170936
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)