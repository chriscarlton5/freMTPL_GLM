"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_best_plus_learning_rate",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Based on best run (tuned aggressive 0.1841 Gini) with slight "
        "learning rate adjustment. Higher learning rate may find better optima."
    ),
    "hypothesis": (
        "Tuned aggressive achieved 0.1841 Gini but narrowly missed 0.005 threshold. "
        "Try slightly higher learning rate to find better local minimum."
    ),
    "actuarial_rationale": (
        "Standard practice to tune learning rate. With early stopping, higher rate "
        "is safe. Full documentation maintained."
    ),
    "lightgbm": {
        "nrounds": 115,
        "early_stopping_rounds": 14,
        "frequency_grid": [
            {
                "num_leaves": 14,
                "min_data_in_leaf": 1700,
                "learning_rate": 0.038,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 11,
            },
            {
                "num_leaves": 22,
                "min_data_in_leaf": 1400,
                "learning_rate": 0.03,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 200,
                "learning_rate": 0.038,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 160,
                "learning_rate": 0.03,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 7,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 200,
                "learning_rate": 0.038,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 160,
                "learning_rate": 0.03,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 7,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
