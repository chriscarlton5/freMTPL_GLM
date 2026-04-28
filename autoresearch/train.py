from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0004",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.511 L2=12.9",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 14,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5112957958775369,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 12.92027389857105
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46129579587753694,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 10.92027389857105
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5112957958775369,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 10.92027389857105
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46129579587753694,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 9.92027389857105
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5112957958775369,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 10.92027389857105
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46129579587753694,
        "bagging_fraction": 0.5112957958775369,
        "lambda_l2": 9.92027389857105
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
