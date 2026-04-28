from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0001",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.521 L2=13.0 L=16",
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
        "feature_fraction": 0.5211096852411505,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 13.025001592752773
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.47110968524115054,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 11.025001592752773
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5211096852411505,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 11.025001592752773
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.47110968524115054,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 10.025001592752773
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5211096852411505,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 11.025001592752773
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.47110968524115054,
        "bagging_fraction": 0.5211096852411505,
        "lambda_l2": 10.025001592752773
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)