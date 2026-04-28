from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0012",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.495 L2=11.1",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 14,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4954536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 11.1018148234603
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4454536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 9.1018148234603
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4954536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 9.1018148234603
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4454536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 8.1018148234603
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4954536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 9.1018148234603
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4454536917459404,
        "bagging_fraction": 0.4954536917459404,
        "lambda_l2": 8.1018148234603
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)