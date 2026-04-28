from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0014",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.512 L2=12.9",
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
        "feature_fraction": 0.5119935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 12.87111953746493
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 10.87111953746493
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5119935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 10.87111953746493
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 9.87111953746493
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5119935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 10.87111953746493
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619935469786833,
        "bagging_fraction": 0.5119935469786833,
        "lambda_l2": 9.87111953746493
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)