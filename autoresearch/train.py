"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0015",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: fewer_leaves. FF=0.502, L2=12.5, leaves=12",
  "hypothesis": "Exploration: fewer_leaves",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 12,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5024303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 12.473715033443145
      },
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4524303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 10.473715033443145
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5024303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 10.473715033443145
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4524303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 9.473715033443145
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5024303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 10.473715033443145
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.4524303746493476,
        "bagging_fraction": 0.5024303746493476,
        "lambda_l2": 9.473715033443145
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
