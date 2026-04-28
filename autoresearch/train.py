"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_optimal_balance_v2",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Combine findings: aggressive LR (0.05) with best settings (leaves 15/24). "
        "Best MAE was 216.90 with 0.1836 Gini. Try to get both."
    ),
    "hypothesis": (
        "Combine optimal LR with optimal leaves. May get best of both."
    ),
    "actuarial_rationale": (
        "Synthesis of best hyperparameters."
    ),
    "lightgbm": {
        "nrounds": 100,
        "early_stopping_rounds": 12,
        "frequency_grid": [
            {
                "num_leaves": 15,
                "min_data_in_leaf": 1800,
                "learning_rate": 0.05,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 11,
            },
            {
                "num_leaves": 24,
                "min_data_in_leaf": 1400,
                "learning_rate": 0.044,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 200,
                "learning_rate": 0.05,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 160,
                "learning_rate": 0.044,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 7,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 200,
                "learning_rate": 0.05,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 9,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 160,
                "learning_rate": 0.044,
                "feature_fraction": 0.81,
                "bagging_fraction": 0.86,
                "lambda_l2": 7,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
