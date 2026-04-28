"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0009",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: different_l2. FF=0.506, L2=9.1, leaves=16",
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
        "feature_fraction": 0.5059966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 9.104474364097575
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4559966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 7.104474364097575
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5059966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 7.104474364097575
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4559966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 6.104474364097575
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5059966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 7.104474364097575
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4559966344511001,
        "bagging_fraction": 0.5059966344511001,
        "lambda_l2": 6.104474364097575
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
