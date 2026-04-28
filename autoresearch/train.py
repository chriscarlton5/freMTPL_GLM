from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0015",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.508 L2=12.7",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5080371828276454,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 12.73818090564429
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45803718282764544,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 10.73818090564429
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5080371828276454,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 10.73818090564429
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45803718282764544,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 9.73818090564429
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5080371828276454,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 10.73818090564429
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45803718282764544,
        "bagging_fraction": 0.5080371828276454,
        "lambda_l2": 9.73818090564429
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
