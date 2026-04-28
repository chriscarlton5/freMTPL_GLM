"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_tuned_midleaf_stronger_capped",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger using a slightly more assertive mid-leaf frequency "
        "option with the stronger forced capped-severity grid that nearly "
        "cleared the segmentation gate."
    ),
    "hypothesis": (
        "The stronger capped candidate missed the Gini gate by 0.0002. A small "
        "frequency learning-rate adjustment may add the remaining ranking lift "
        "while preserving the all-fold improvement pattern."
    ),
    "actuarial_rationale": (
        "This is a local sensitivity test around the best near miss. It remains "
        "segmentation research only and should be discarded unless the lift "
        "clears the predefined threshold without calibration or fold weakness."
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
            {
                "num_leaves": 31,
                "min_data_in_leaf": 500,
                "learning_rate": 0.06,
                "feature_fraction": 0.8,
                "bagging_fraction": 0.8,
                "lambda_l2": 5,
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
                "num_leaves": 63,
                "min_data_in_leaf": 75,
                "learning_rate": 0.025,
                "feature_fraction": 0.75,
                "bagging_fraction": 0.9,
                "lambda_l2": 12,
            },
            {
                "num_leaves": 63,
                "min_data_in_leaf": 50,
                "learning_rate": 0.02,
                "feature_fraction": 0.7,
                "bagging_fraction": 0.85,
                "lambda_l2": 18,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
