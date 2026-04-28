"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_optimal_exploration",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Final exploration: 18 leaves at 0.048 LR, extreme L2=15 for safety. "
        "Testing boundary of hyperparameter space."
    ),
    "hypothesis": (
        "Push to boundary to find potential new optimum. High L2 prevents wild fits."
    ),
    "actuarial_rationale": (
        "Final boundary test."
    ),
    "lightgbm": {
        "nrounds": 130,
        "early_stopping_rounds": 18,
        "frequency_grid": [
            {
                "num_leaves": 18,
                "min_data_in_leaf": 1700,
                "learning_rate": 0.048,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 15,
            },
            {
                "num_leaves": 26,
                "min_data_in_leaf": 1350,
                "learning_rate": 0.042,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 12,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 200,
                "learning_rate": 0.048,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 12,
            },
            {
                "num_leaves": 12,
                "min_data_in_leaf": 160,
                "learning_rate": 0.042,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 10,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 200,
                "learning_rate": 0.048,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 12,
            },
            {
                "num_leaves": 12,
                "min_data_in_leaf": 160,
                "learning_rate": 0.042,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 10,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
