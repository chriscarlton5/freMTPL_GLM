from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0006",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "EXPLORE: FF=0.482, L2=11.2, leaves=19",
  "hypothesis": "EXPLORE approach",
  "actuarial_rationale": "Autonomous exploration",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 19,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4817886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 11.238936958692936
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4317886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 9.238936958692936
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4817886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 9.238936958692936
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4317886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 8.238936958692936
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4817886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 9.238936958692936
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4317886591579052,
        "bagging_fraction": 0.4817886591579052,
        "lambda_l2": 8.238936958692936
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)