from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0019",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.509 L2=13.0",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5092090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 12.975118419318727
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4592090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 10.975118419318727
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5092090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 10.975118419318727
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4592090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 9.975118419318727
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5092090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 10.975118419318727
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4592090599357486,
        "bagging_fraction": 0.5092090599357486,
        "lambda_l2": 9.975118419318727
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)