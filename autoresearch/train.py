from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.534 L2=14.6",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5339202895912422,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 14.585332069460318
      },
      {
        "num_leaves": 30,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.48392028959124217,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 12.585332069460318
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5339202895912422,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 12.585332069460318
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48392028959124217,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 11.585332069460318
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5339202895912422,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 12.585332069460318
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48392028959124217,
        "bagging_fraction": 0.5339202895912422,
        "lambda_l2": 11.585332069460318
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)