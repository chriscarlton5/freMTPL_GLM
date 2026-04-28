"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_lower_lr_more_iter",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Best 0.1851 with leaves 15/24, LR 0.04/0.035. Try lower LR (0.03/0.025) "
        "with more rounds for more stable convergence."
    ),
    "hypothesis": (
        "Lower LR + more iterations may find better local minimum. "
        "Standard tuning practice."
    ),
    "actuarial_rationale": (
        "Slower learning with more iterations for better convergence."
    ),
    "lightgbm": {
        "nrounds": 180,
        "early_stopping_rounds": 20,
        "frequency_grid": [
            {
                "num_leaves": 15,
                "min_data_in_leaf": 1550,
                "learning_rate": 0.03,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 24,
                "min_data_in_leaf": 1250,
                "learning_rate": 0.025,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 180,
                "learning_rate": 0.03,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 140,
                "learning_rate": 0.025,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 180,
                "learning_rate": 0.03,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 140,
                "learning_rate": 0.025,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
