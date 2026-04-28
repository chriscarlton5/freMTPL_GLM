from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_explore_0019",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "EXPLORE: FF=0.523 L2=10.2 L=21",
  "hypothesis": "EXPLORE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 21,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5227621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 10.17720573325338
      },
      {
        "num_leaves": 29,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 8.17720573325338
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5227621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 8.17720573325338
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 7.1772057332533805
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5227621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 8.17720573325338
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727621884600938,
        "bagging_fraction": 0.5227621884600938,
        "lambda_l2": 7.1772057332533805
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)