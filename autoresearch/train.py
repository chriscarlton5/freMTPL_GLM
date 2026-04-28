from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0025",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.509 L2=12.9",
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
        "feature_fraction": 0.5087322853651955,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 12.905892324884766
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45873228536519556,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 10.905892324884766
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5087322853651955,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 10.905892324884766
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45873228536519556,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 9.905892324884766
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5087322853651955,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 10.905892324884766
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45873228536519556,
        "bagging_fraction": 0.5087322853651955,
        "lambda_l2": 9.905892324884766
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
