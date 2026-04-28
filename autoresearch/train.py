from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0017",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.483 L2=11.8",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 19,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4830378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 11.84375968703081
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4330378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 9.84375968703081
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4830378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 9.84375968703081
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4330378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 8.84375968703081
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4830378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 9.84375968703081
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4330378049771179,
        "bagging_fraction": 0.4830378049771179,
        "lambda_l2": 8.84375968703081
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)