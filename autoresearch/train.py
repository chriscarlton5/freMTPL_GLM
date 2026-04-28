from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0002",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.508 L2=14.6",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5079885397470618,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 14.603857492408652
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45798853974706183,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 12.603857492408652
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5079885397470618,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 12.603857492408652
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45798853974706183,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 11.603857492408652
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5079885397470618,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 12.603857492408652
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45798853974706183,
        "bagging_fraction": 0.5079885397470618,
        "lambda_l2": 11.603857492408652
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
