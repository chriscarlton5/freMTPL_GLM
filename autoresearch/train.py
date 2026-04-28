from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0029",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.518 L2=13.1",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.517604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 13.1355890045533
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.467604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 11.1355890045533
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.517604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 11.1355890045533
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.467604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 10.1355890045533
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.517604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 11.1355890045533
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.467604538749728,
        "bagging_fraction": 0.517604538749728,
        "lambda_l2": 10.1355890045533
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
