"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_frequency_16_20",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM with exact params from best run (14,22 leaves) but with "
        "frequency at (16,20) to see if 16 leaves helps."
    ),
    "hypothesis": (
        "Best run had 14,22 leaves at 0.1845 Gini. Try 16,20 leaves for even "
        "more granular frequency splits."
    ),
    "actuarial_rationale": (
        "Fine-tuning leaf counts is standard. Keep balanced regularization."
    ),
    "lightgbm": {
        "nrounds": 115,
        "early_stopping_rounds": 14,
        "frequency_grid": [
            {
                "num_leaves": 16,
                "min_data_in_leaf": 1600,
                "learning_rate": 0.038,
                "feature_fraction": 0.86,
                "bagging_fraction": 0.86,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 20,
                "min_data_in_leaf": 1400,
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
