"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_midleaf_frequency_stronger_capped",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger combining the mid-leaf frequency probe with a "
        "stronger forced capped-severity grid to test whether the recent "
        "near-miss can clear the segmentation Gini threshold."
    ),
    "hypothesis": (
        "The forced aggressive capped candidate passed fold agreement and "
        "reached capped Gini 0.1864. Slightly stronger capped-severity "
        "flexibility may add the remaining lift needed to clear the 0.005 "
        "champion gain gate without breaking calibration."
    ),
    "actuarial_rationale": (
        "This is a high-risk segmentation-only experiment. It is acceptable "
        "only if the lift remains broad across folds; otherwise it is evidence "
        "that capped severity flexibility is no longer actuarially defensible."
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
                "learning_rate": 0.05,
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
