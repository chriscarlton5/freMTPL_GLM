from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0014",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.486 L2=16.4",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4855139467332221,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 16.436629093668188
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.43551394673322213,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 14.436629093668188
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4855139467332221,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 14.436629093668188
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43551394673322213,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 13.436629093668188
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4855139467332221,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 14.436629093668188
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43551394673322213,
        "bagging_fraction": 0.4855139467332221,
        "lambda_l2": 13.436629093668188
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
