"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ft_0001",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Fine-tune: leaves. FF=0.515, L2=13.2",
  "hypothesis": "Targeted leaves variation",
  "actuarial_rationale": "Exploiting sweet spot",
  "lightgbm": {
    "nrounds": 178,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5155,
        "bagging_fraction": 0.5155,
        "lambda_l2": 13.2142
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1360,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46549999999999997,
        "bagging_fraction": 0.5155,
        "lambda_l2": 11.2142
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5155,
        "bagging_fraction": 0.5155,
        "lambda_l2": 10.2142
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46549999999999997,
        "bagging_fraction": 0.5155,
        "lambda_l2": 9.2142
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5155,
        "bagging_fraction": 0.5155,
        "lambda_l2": 10.2142
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46549999999999997,
        "bagging_fraction": 0.5155,
        "lambda_l2": 9.2142
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
