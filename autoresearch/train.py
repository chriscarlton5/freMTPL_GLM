from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0007",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.520 L2=12.7",
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
        "feature_fraction": 0.5202180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 12.745622293517018
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4702180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 10.745622293517018
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5202180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 10.745622293517018
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4702180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 9.745622293517018
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5202180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 10.745622293517018
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4702180661613841,
        "bagging_fraction": 0.5202180661613841,
        "lambda_l2": 9.745622293517018
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
