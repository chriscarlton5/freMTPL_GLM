from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0017",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.490 L2=10.3",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.49049594744844605,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 10.257920701945531
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.44049594744844606,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 8.257920701945531
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.49049594744844605,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 8.257920701945531
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.44049594744844606,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 7.257920701945531
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.49049594744844605,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 8.257920701945531
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.44049594744844606,
        "bagging_fraction": 0.49049594744844605,
        "lambda_l2": 7.257920701945531
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
