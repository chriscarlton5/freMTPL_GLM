from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.508, L2=13.3, leaves=16",
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
        "feature_fraction": 0.5082692108811862,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 13.250776467946178
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45826921088118616,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 11.250776467946178
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5082692108811862,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 11.250776467946178
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45826921088118616,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 10.250776467946178
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5082692108811862,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 11.250776467946178
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45826921088118616,
        "bagging_fraction": 0.5082692108811862,
        "lambda_l2": 10.250776467946178
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)