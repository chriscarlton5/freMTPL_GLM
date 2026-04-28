"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ft_0002",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Fine-tune: l2. FF=0.515, L2=13.3",
  "hypothesis": "Targeted l2 variation",
  "actuarial_rationale": "Exploiting sweet spot",
  "lightgbm": {
    "nrounds": 178,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1795,
        "learning_rate": 0.0365,
        "feature_fraction": 0.515,
        "bagging_fraction": 0.515,
        "lambda_l2": 13.294983769259293
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1436,
        "learning_rate": 0.0315,
        "feature_fraction": 0.465,
        "bagging_fraction": 0.515,
        "lambda_l2": 11.294983769259293
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.0365,
        "feature_fraction": 0.515,
        "bagging_fraction": 0.515,
        "lambda_l2": 10.294983769259293
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.0315,
        "feature_fraction": 0.465,
        "bagging_fraction": 0.515,
        "lambda_l2": 9.294983769259293
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.0365,
        "feature_fraction": 0.515,
        "bagging_fraction": 0.515,
        "lambda_l2": 10.294983769259293
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.0315,
        "feature_fraction": 0.465,
        "bagging_fraction": 0.515,
        "lambda_l2": 9.294983769259293
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
