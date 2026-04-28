from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0008",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.485 L2=12.0",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 19,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.48512542035329914,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 11.990243763022683
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.43512542035329915,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 9.990243763022683
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48512542035329914,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 9.990243763022683
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43512542035329915,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 8.990243763022683
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.48512542035329914,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 9.990243763022683
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.43512542035329915,
        "bagging_fraction": 0.48512542035329914,
        "lambda_l2": 8.990243763022683
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)