from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0007",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.539 L2=15.0",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.539302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 15.031626397485809
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.489302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 13.031626397485809
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.539302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 13.031626397485809
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.489302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 12.031626397485809
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.539302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 13.031626397485809
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.489302149043558,
        "bagging_fraction": 0.539302149043558,
        "lambda_l2": 12.031626397485809
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)