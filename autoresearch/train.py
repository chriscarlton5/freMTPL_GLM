"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_0002_autotune",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Auto-generated: fraction variation on champion. FF=0.520, L2=13.4, leaves=16/24",
  "hypothesis": "Fine-tuning fraction from champion config.",
  "actuarial_rationale": "Testing fraction variation for potential improvement.",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1795,
        "learning_rate": 0.0365,
        "feature_fraction": 0.5197054111866342,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 13.4
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1436,
        "learning_rate": 0.0315,
        "feature_fraction": 0.46970541118663417,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 11.4
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 218,
        "learning_rate": 0.0365,
        "feature_fraction": 0.5197054111866342,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 10.4
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 168,
        "learning_rate": 0.0315,
        "feature_fraction": 0.46970541118663417,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 9.4
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 218,
        "learning_rate": 0.0365,
        "feature_fraction": 0.5197054111866342,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 10.4
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 168,
        "learning_rate": 0.0315,
        "feature_fraction": 0.46970541118663417,
        "bagging_fraction": 0.5197054111866342,
        "lambda_l2": 9.4
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
