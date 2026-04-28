from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0001",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.510 L2=13.2",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5102517511978228,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 13.207641906214516
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46025175119782286,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 11.207641906214516
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5102517511978228,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 11.207641906214516
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46025175119782286,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 10.207641906214516
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5102517511978228,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 11.207641906214516
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46025175119782286,
        "bagging_fraction": 0.5102517511978228,
        "lambda_l2": 10.207641906214516
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
