from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0016",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.535 L2=14.8",
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
        "feature_fraction": 0.5347649355259044,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 14.807730181923427
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.48476493552590444,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 12.807730181923427
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5347649355259044,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 12.807730181923427
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48476493552590444,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 11.807730181923427
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5347649355259044,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 12.807730181923427
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48476493552590444,
        "bagging_fraction": 0.5347649355259044,
        "lambda_l2": 11.807730181923427
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)