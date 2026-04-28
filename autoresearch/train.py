"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_even_more_leaves",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Best now at Gini 0.1851, -0.98% calibration. Try more leaves (16-28) "
        "to capture more complex patterns."
    ),
    "hypothesis": (
        "Previous run 0.1851 was better. Try more leaves for more capacity. "
        "May capture finer risk segments."
    ),
    "actuarial_rationale": (
        "More leaves = more capacity. Keep regularization high to prevent overfit."
    ),
    "lightgbm": {
        "nrounds": 120,
        "early_stopping_rounds": 15,
        "frequency_grid": [
            {
                "num_leaves": 16,
                "min_data_in_leaf": 1500,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 28,
                "min_data_in_leaf": 1200,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 180,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 12,
                "min_data_in_leaf": 140,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 8,
                "min_data_in_leaf": 180,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 12,
                "min_data_in_leaf": 140,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
