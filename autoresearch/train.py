"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_optimal_balance",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Best still 0.1851. Try intermediate: 16/23 leaves, 0.042 LR to find "
        "optimum between capacity and overfitting."
    ),
    "hypothesis": (
        "15/24 @ 0.04 = 0.1851, 16/28 @ 0.04 = 0.1834. Try 16/23 with 0.042 LR."
    ),
    "actuarial_rationale": (
        "Balance between best configs - fine-tuned hyperparameter search."
    ),
    "lightgbm": {
        "nrounds": 125,
        "early_stopping_rounds": 16,
        "frequency_grid": [
            {
                "num_leaves": 16,
                "min_data_in_leaf": 1550,
                "learning_rate": 0.042,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 23,
                "min_data_in_leaf": 1250,
                "learning_rate": 0.036,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 170,
                "learning_rate": 0.042,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 130,
                "learning_rate": 0.036,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 170,
                "learning_rate": 0.042,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 130,
                "learning_rate": 0.036,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
