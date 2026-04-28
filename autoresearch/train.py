from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0027",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.512 L2=11.5",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.512305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 11.487799834462066
      },
      {
        "num_leaves": 28,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.462305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 9.487799834462066
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.512305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 9.487799834462066
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.462305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 8.487799834462066
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.512305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 9.487799834462066
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.462305872497537,
        "bagging_fraction": 0.512305872497537,
        "lambda_l2": 8.487799834462066
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
