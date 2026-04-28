from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0019",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.480 L2=17.9",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 17.86037963955095
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 15.860379639550949
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 15.860379639550949
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 14.860379639550949
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48,
        "bagging_fraction": 0.48,
        "lambda_l2": 15.860379639550949
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43,
        "bagging_fraction": 0.48,
        "lambda_l2": 14.860379639550949
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
