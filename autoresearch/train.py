from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0010",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.513 L2=12.7 L=17",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.512805432946059,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 12.742697707664272
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46280543294605897,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 10.742697707664272
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.512805432946059,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 10.742697707664272
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46280543294605897,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 9.742697707664272
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.512805432946059,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 10.742697707664272
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46280543294605897,
        "bagging_fraction": 0.512805432946059,
        "lambda_l2": 9.742697707664272
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)