"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0020",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: very_low_ff. FF=0.457, L2=14.4, leaves=17",
  "hypothesis": "Exploration: very_low_ff",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.45721302133896335,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 14.386042215717582
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.40721302133896337,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 12.386042215717582
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.45721302133896335,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 12.386042215717582
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.40721302133896337,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 11.386042215717582
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.45721302133896335,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 12.386042215717582
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.40721302133896337,
        "bagging_fraction": 0.45721302133896335,
        "lambda_l2": 11.386042215717582
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
