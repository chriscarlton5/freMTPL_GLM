from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0024",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.534 L2=10.6",
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
        "feature_fraction": 0.534474546333577,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 10.608583508250451
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.48447454633357706,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 8.608583508250451
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.534474546333577,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 8.608583508250451
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48447454633357706,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 7.608583508250451
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.534474546333577,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 8.608583508250451
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48447454633357706,
        "bagging_fraction": 0.534474546333577,
        "lambda_l2": 7.608583508250451
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
