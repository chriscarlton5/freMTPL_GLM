"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_flexible_capped_severity",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Regularized LightGBM challenger that keeps the current frequency and "
        "raw severity grids but gives capped severity a more flexible grid."
    ),
    "hypothesis": (
        "The segmentation champion may be limited by capped-severity ranking. "
        "A more flexible capped-severity component may improve capped pure "
        "premium Gini without weakening frequency or raw severity behavior."
    ),
    "actuarial_rationale": (
        "Capped severity is the stability-oriented severity view. Flexibility is "
        "increased only there, while the frequency and raw severity components "
        "remain on the current constrained grids."
    ),
    "lightgbm": {
        "nrounds": 150,
        "early_stopping_rounds": 20,
        "frequency_grid": [
            {
                "num_leaves": 15,
                "min_data_in_leaf": 1200,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
            {
                "num_leaves": 31,
                "min_data_in_leaf": 1500,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 150,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
            {
                "num_leaves": 15,
                "min_data_in_leaf": 200,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 31,
                "min_data_in_leaf": 100,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
            {
                "num_leaves": 63,
                "min_data_in_leaf": 150,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
