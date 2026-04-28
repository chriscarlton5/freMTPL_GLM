"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ft_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Fine-tune: min_data. FF=0.518, L2=13.2",
  "hypothesis": "Targeted min_data variation",
  "actuarial_rationale": "Exploiting sweet spot",
  "lightgbm": {
    "nrounds": 178,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1600,
        "learning_rate": 0.036,
        "feature_fraction": 0.5179,
        "bagging_fraction": 0.5179,
        "lambda_l2": 13.2142
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1280,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46790000000000004,
        "bagging_fraction": 0.5179,
        "lambda_l2": 11.2142
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5179,
        "bagging_fraction": 0.5179,
        "lambda_l2": 10.2142
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46790000000000004,
        "bagging_fraction": 0.5179,
        "lambda_l2": 9.2142
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 215,
        "learning_rate": 0.036,
        "feature_fraction": 0.5179,
        "bagging_fraction": 0.5179,
        "lambda_l2": 10.2142
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 165,
        "learning_rate": 0.030999999999999996,
        "feature_fraction": 0.46790000000000004,
        "bagging_fraction": 0.5179,
        "lambda_l2": 9.2142
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
