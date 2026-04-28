from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0020",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.515 L2=12.6",
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
        "feature_fraction": 0.5149163939120129,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 12.649252914592413
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46491639391201295,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 10.649252914592413
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5149163939120129,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 10.649252914592413
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46491639391201295,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 9.649252914592413
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5149163939120129,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 10.649252914592413
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46491639391201295,
        "bagging_fraction": 0.5149163939120129,
        "lambda_l2": 9.649252914592413
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
