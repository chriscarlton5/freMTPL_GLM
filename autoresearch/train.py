from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0009",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.480 L2=14.6",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 12,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 14.558073346704251
      },
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 12.558073346704251
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 12.558073346704251
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 11.558073346704251
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 12.558073346704251
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 11.558073346704251
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)