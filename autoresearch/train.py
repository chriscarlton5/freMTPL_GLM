from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0005",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.518 L2=12.9 L=18",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5176419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 12.929587256204735
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4676419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 10.929587256204735
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5176419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 10.929587256204735
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4676419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 9.929587256204735
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5176419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 10.929587256204735
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4676419859376228,
        "bagging_fraction": 0.5176419859376228,
        "lambda_l2": 9.929587256204735
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)