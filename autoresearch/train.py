from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0033",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.504 L2=10.4",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 21,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5041516158229649,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 10.435155718327977
      },
      {
        "num_leaves": 29,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45415161582296487,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 8.435155718327977
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5041516158229649,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 8.435155718327977
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45415161582296487,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 7.435155718327977
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5041516158229649,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 8.435155718327977
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45415161582296487,
        "bagging_fraction": 0.5041516158229649,
        "lambda_l2": 7.435155718327977
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
