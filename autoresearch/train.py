from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0009",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.511 L2=13.0 L=15",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5105398078722528,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 12.952372403257895
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46053980787225285,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 10.952372403257895
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5105398078722528,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 10.952372403257895
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46053980787225285,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 9.952372403257895
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5105398078722528,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 10.952372403257895
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46053980787225285,
        "bagging_fraction": 0.5105398078722528,
        "lambda_l2": 9.952372403257895
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)