"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0010",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: higher_ff. FF=0.538, L2=10.8, leaves=20",
  "hypothesis": "Exploration: higher_ff",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5377441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 10.758779121801672
      },
      {
        "num_leaves": 28,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4877441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 8.758779121801672
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5377441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 8.758779121801672
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4877441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 7.7587791218016715
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5377441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 8.758779121801672
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4877441420393211,
        "bagging_fraction": 0.5377441420393211,
        "lambda_l2": 7.7587791218016715
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
