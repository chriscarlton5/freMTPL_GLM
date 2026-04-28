from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0016",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.510 L2=13.3 L=16",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5104624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 13.258749984161273
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4604624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 11.258749984161273
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5104624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 11.258749984161273
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4604624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 10.258749984161273
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5104624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 11.258749984161273
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4604624588271889,
        "bagging_fraction": 0.5104624588271889,
        "lambda_l2": 10.258749984161273
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)