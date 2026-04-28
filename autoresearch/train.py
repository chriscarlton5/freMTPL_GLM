"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0016",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: very_low_ff. FF=0.469, L2=13.6, leaves=16",
  "hypothesis": "Exploration: very_low_ff",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4693763040737877,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 13.562493787088208
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.41937630407378773,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 11.562493787088208
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.4693763040737877,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 11.562493787088208
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.41937630407378773,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 10.562493787088208
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.4693763040737877,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 11.562493787088208
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.41937630407378773,
        "bagging_fraction": 0.4693763040737877,
        "lambda_l2": 10.562493787088208
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
