from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0006",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.522 L2=12.9",
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
        "feature_fraction": 0.5218799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 12.880276022142349
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 10.880276022142349
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5218799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 10.880276022142349
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 9.880276022142349
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5218799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 10.880276022142349
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718799247307734,
        "bagging_fraction": 0.5218799247307734,
        "lambda_l2": 9.880276022142349
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)