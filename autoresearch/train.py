from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0012",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.518 L2=12.6",
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
        "feature_fraction": 0.5178904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 12.628895521216458
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4678904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 10.628895521216458
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5178904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 10.628895521216458
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4678904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 9.628895521216458
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5178904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 10.628895521216458
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4678904481886779,
        "bagging_fraction": 0.5178904481886779,
        "lambda_l2": 9.628895521216458
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
