from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0004",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.518, L2=13.4, leaves=15",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous exploration",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5184060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 13.35160768906937
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4684060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 11.35160768906937
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5184060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 11.35160768906937
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4684060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 10.35160768906937
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5184060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 11.35160768906937
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4684060634779677,
        "bagging_fraction": 0.5184060634779677,
        "lambda_l2": 10.35160768906937
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)