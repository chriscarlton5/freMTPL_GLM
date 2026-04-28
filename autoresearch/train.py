from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0005",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.507 L2=13.2",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5071607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 13.186534831794454
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4571607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 11.186534831794454
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5071607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 11.186534831794454
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4571607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 10.186534831794454
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5071607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 11.186534831794454
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4571607617774079,
        "bagging_fraction": 0.5071607617774079,
        "lambda_l2": 10.186534831794454
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
