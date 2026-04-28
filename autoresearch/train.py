from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0032",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.484 L2=16.0",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 21,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4840993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 15.973208662570269
      },
      {
        "num_leaves": 29,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4340993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 13.973208662570269
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4840993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 13.973208662570269
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4340993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 12.973208662570269
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4840993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 13.973208662570269
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4340993330908563,
        "bagging_fraction": 0.4840993330908563,
        "lambda_l2": 12.973208662570269
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
