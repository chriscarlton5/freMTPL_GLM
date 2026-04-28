"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_frequency_deeper",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM with more leaves on frequency (16-24), regular severity (6-10). "
        "Frequency drives Gini - give it more capacity."
    ),
    "hypothesis": (
        "Frequency is the main Gini driver. Previous best was at 14-22 leaves. "
        "Try 16-24 to see if more capacity helps."
    ),
    "actuarial_rationale": (
        "Focus capacity where signal is strongest - standard practice. "
        "Severity keeps regularization."
    ),
    "lightgbm": {
        "nrounds": 115,
        "early_stopping_rounds": 14,
        "frequency_grid": [
            {
                "num_leaves": 16,
                "min_data_in_leaf": 1500,
                "learning_rate": 0.038,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 24,
                "min_data_in_leaf": 1300,
                "learning_rate": 0.032,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.86,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 6,
                "min_data_in_leaf": 180,
                "learning_rate": 0.036,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 10,
                "min_data_in_leaf": 150,
                "learning_rate": 0.03,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.86,
                "lambda_l2": 6,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 6,
                "min_data_in_leaf": 180,
                "learning_rate": 0.036,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 10,
                "min_data_in_leaf": 150,
                "learning_rate": 0.03,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.86,
                "lambda_l2": 6,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
