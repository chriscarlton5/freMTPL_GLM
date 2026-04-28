from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0015",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.512 L2=13.1",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 13.101858333345733
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 11.101858333345733
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 11.101858333345733
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 10.101858333345733
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 11.101858333345733
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623937082807898,
        "bagging_fraction": 0.5123937082807898,
        "lambda_l2": 10.101858333345733
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)