"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_moderate_capped_severity_push",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger that preserves the current frequency and raw "
        "severity grids while adding moderate capped-severity flexibility "
        "between the prior flexible and aggressive attempts."
    ),
    "hypothesis": (
        "The flexible capped-severity run improved two folds but not enough "
        "on mean Gini, while the aggressive run lifted mean Gini mostly through "
        "fold 3. A moderate capped-severity grid may increase mean capped Gini "
        "without sacrificing fold 1 or fold 2."
    ),
    "actuarial_rationale": (
        "This is segmentation research only. It keeps the more stable frequency "
        "signal fixed and tests whether capped severity can add controlled lift "
        "without creating an unsupported black-box severity artifact."
    ),
    "lightgbm": {
        "nrounds": 120,
        "early_stopping_rounds": 15,
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
            {
                "num_leaves": 31,
                "min_data_in_leaf": 140,
                "learning_rate": 0.03,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.9,
                "lambda_l2": 12,
            },
            {
                "num_leaves": 31,
                "min_data_in_leaf": 180,
                "learning_rate": 0.025,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 15,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
