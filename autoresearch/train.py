"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0017",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: balanced. FF=0.512, L2=13.5, leaves=17",
  "hypothesis": "Exploration: balanced",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 13.467486156106052
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 11.467486156106052
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 11.467486156106052
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 10.467486156106052
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 11.467486156106052
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4623211712276581,
        "bagging_fraction": 0.5123211712276581,
        "lambda_l2": 10.467486156106052
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
