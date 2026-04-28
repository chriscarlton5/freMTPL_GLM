"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ft_0007",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Fine-tune: combo. FF=0.510, L2=13.6",
  "hypothesis": "Targeted combo variation",
  "actuarial_rationale": "Exploiting sweet spot",
  "lightgbm": {
    "nrounds": 178,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5096019204260099,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 13.647602467561022
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1360,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.45960192042600995,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 11.647602467561022
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5096019204260099,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 10.647602467561022
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.45960192042600995,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 9.647602467561022
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5096019204260099,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 10.647602467561022
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.45960192042600995,
        "bagging_fraction": 0.5096019204260099,
        "lambda_l2": 9.647602467561022
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
