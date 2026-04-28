from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0005",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.517, L2=12.6, leaves=16",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous exploration",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5165084034677809,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 12.593898609118419
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46650840346778094,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 10.593898609118419
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5165084034677809,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 10.593898609118419
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46650840346778094,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 9.593898609118419
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5165084034677809,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 10.593898609118419
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46650840346778094,
        "bagging_fraction": 0.5165084034677809,
        "lambda_l2": 9.593898609118419
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)