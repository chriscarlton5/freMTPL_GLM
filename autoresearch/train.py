from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0020",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.491 L2=12.8",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4910682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 12.839329856417338
      },
      {
        "num_leaves": 28,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4410682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 10.839329856417338
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4910682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 10.839329856417338
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4410682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 9.839329856417338
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4910682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 10.839329856417338
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4410682924012371,
        "bagging_fraction": 0.4910682924012371,
        "lambda_l2": 9.839329856417338
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)