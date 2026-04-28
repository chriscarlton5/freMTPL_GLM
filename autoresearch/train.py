"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
  "id": "lightgbm_ex_0018",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "Explore: more_leaves. FF=0.519, L2=12.4, leaves=24",
  "hypothesis": "Exploration: more_leaves",
  "actuarial_rationale": "Breaking plateau with new direction",
  "lightgbm": {
    "nrounds": 180,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5187911652472664,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 12.411053484890598
      },
      {
        "num_leaves": 32,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46879116524726644,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 10.411053484890598
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5187911652472664,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 10.411053484890598
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.46879116524726644,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 9.411053484890598
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 205,
        "learning_rate": 0.036,
        "feature_fraction": 0.5187911652472664,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 10.411053484890598
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 155,
        "learning_rate": 0.031,
        "feature_fraction": 0.46879116524726644,
        "bagging_fraction": 0.5187911652472664,
        "lambda_l2": 9.411053484890598
      }
    ]
  }
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
