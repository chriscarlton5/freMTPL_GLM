"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ft_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Fine-tune: leaves. FF=0.512, L2=13.5",
  "hypothesis": "Targeted leaves variation",
  "actuarial_rationale": "Exploiting sweet spot",
  "lightgbm": {
    "nrounds": 178,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123,
        "bagging_fraction": 0.5123,
        "lambda_l2": 13.4675
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1360,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.4623,
        "bagging_fraction": 0.5123,
        "lambda_l2": 11.4675
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123,
        "bagging_fraction": 0.5123,
        "lambda_l2": 10.4675
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.4623,
        "bagging_fraction": 0.5123,
        "lambda_l2": 9.4675
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5123,
        "bagging_fraction": 0.5123,
        "lambda_l2": 10.4675
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.4623,
        "bagging_fraction": 0.5123,
        "lambda_l2": 9.4675
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
