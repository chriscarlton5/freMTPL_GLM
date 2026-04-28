from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0009",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.508 L2=13.0",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 14,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5076470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 13.018942501328047
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4576470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 11.018942501328047
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5076470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 11.018942501328047
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4576470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 10.018942501328047
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5076470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 11.018942501328047
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4576470948877827,
        "bagging_fraction": 0.5076470948877827,
        "lambda_l2": 10.018942501328047
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
