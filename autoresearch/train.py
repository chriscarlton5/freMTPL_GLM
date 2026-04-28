"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0019",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: higher_ff. FF=0.527, L2=11.4, leaves=16",
  "hypothesis": "Exploration: higher_ff",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5269359492420723,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 11.354417704694818
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.47693594924207233,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 9.354417704694818
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5269359492420723,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 9.354417704694818
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.47693594924207233,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 8.354417704694818
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5269359492420723,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 9.354417704694818
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.47693594924207233,
        "bagging_fraction": 0.5269359492420723,
        "lambda_l2": 8.354417704694818
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
