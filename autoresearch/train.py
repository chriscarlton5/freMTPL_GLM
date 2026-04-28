"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0014",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: balanced. FF=0.517, L2=11.4, leaves=18",
  "hypothesis": "Exploration: balanced",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5168384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 11.436305219575567
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4668384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 9.436305219575567
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5168384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 9.436305219575567
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4668384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 8.436305219575567
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5168384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 9.436305219575567
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4668384600105297,
        "bagging_fraction": 0.5168384600105297,
        "lambda_l2": 8.436305219575567
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
