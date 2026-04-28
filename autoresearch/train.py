from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0008",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.485 L2=13.1",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 13,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4849919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 13.054498024900003
      },
      {
        "num_leaves": 21,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4349919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 11.054498024900003
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4849919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 11.054498024900003
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4349919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 10.054498024900003
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4849919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 11.054498024900003
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4349919014505306,
        "bagging_fraction": 0.4849919014505306,
        "lambda_l2": 10.054498024900003
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
