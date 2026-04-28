from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_explore_0004",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "EXPLORE: FF=0.520 L2=13.2 L=17",
  "hypothesis": "EXPLORE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5196397164788493,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 13.181174370729126
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46963971647884933,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 11.181174370729126
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5196397164788493,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 11.181174370729126
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46963971647884933,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 10.181174370729126
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5196397164788493,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 11.181174370729126
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46963971647884933,
        "bagging_fraction": 0.5196397164788493,
        "lambda_l2": 10.181174370729126
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)