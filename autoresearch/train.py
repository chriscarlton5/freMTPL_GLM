"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0013",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: different_l2. FF=0.502, L2=9.7, leaves=16",
  "hypothesis": "Exploration: different_l2",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5020167700039093,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 9.730671205268408
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45201677000390933,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 7.730671205268408
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5020167700039093,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 7.730671205268408
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.45201677000390933,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 6.730671205268408
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5020167700039093,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 7.730671205268408
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.45201677000390933,
        "bagging_fraction": 0.5020167700039093,
        "lambda_l2": 6.730671205268408
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
