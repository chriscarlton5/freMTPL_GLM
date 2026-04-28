from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0012",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.510 L2=12.7 L=15",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.510357741559993,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 12.69923550686781
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46035774155999304,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 10.69923550686781
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.510357741559993,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 10.69923550686781
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46035774155999304,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 9.69923550686781
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.510357741559993,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 10.69923550686781
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46035774155999304,
        "bagging_fraction": 0.510357741559993,
        "lambda_l2": 9.69923550686781
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)