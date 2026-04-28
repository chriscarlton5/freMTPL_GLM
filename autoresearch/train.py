from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0010",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.518 L2=12.7",
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
        "feature_fraction": 0.5182657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 12.748625598705237
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 10.748625598705237
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5182657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 10.748625598705237
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 9.748625598705237
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5182657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 10.748625598705237
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682657375724581,
        "bagging_fraction": 0.5182657375724581,
        "lambda_l2": 9.748625598705237
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
