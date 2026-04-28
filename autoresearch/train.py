from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0002",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.482 L2=16.8",
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
        "feature_fraction": 0.48159180678178115,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 16.81075573630682
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.43159180678178116,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 14.81075573630682
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48159180678178115,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 14.81075573630682
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43159180678178116,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 13.81075573630682
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48159180678178115,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 14.81075573630682
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43159180678178116,
        "bagging_fraction": 0.48159180678178115,
        "lambda_l2": 13.81075573630682
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)