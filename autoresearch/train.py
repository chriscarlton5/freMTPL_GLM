from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.522 L2=13.3 L=14",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 14,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5218389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 13.345678051421144
      },
      {
        "num_leaves": 22,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 11.345678051421144
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5218389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 11.345678051421144
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 10.345678051421144
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5218389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 11.345678051421144
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4718389760467065,
        "bagging_fraction": 0.5218389760467065,
        "lambda_l2": 10.345678051421144
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)