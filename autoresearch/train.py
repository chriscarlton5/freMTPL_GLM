from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0014",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.518 L2=13.0 L=16",
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
        "feature_fraction": 0.5182156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 12.95494422290276
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 10.95494422290276
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5182156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 10.95494422290276
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 9.95494422290276
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5182156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 10.95494422290276
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4682156626613138,
        "bagging_fraction": 0.5182156626613138,
        "lambda_l2": 9.95494422290276
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)