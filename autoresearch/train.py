"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0009",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: different_lr. FF=0.520, L2=13.3, leaves=15",
  "hypothesis": "Exploration: different_lr",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5197304698501964,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 13.338479462727777
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46973046985019645,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 11.338479462727777
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5197304698501964,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 11.338479462727777
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.46973046985019645,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 10.338479462727777
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5197304698501964,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 11.338479462727777
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.46973046985019645,
        "bagging_fraction": 0.5197304698501964,
        "lambda_l2": 10.338479462727777
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
