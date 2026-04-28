from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0011",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.514 L2=12.9",
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
        "feature_fraction": 0.514251600118461,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 12.898408463598152
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46425160011846106,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 10.898408463598152
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.514251600118461,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 10.898408463598152
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46425160011846106,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 9.898408463598152
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.514251600118461,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 10.898408463598152
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46425160011846106,
        "bagging_fraction": 0.514251600118461,
        "lambda_l2": 9.898408463598152
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)