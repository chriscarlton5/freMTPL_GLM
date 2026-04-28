"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_midleaf_frequency_forced_aggressive_capped",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger combining the mid-leaf frequency probe with a "
        "forced aggressive capped-severity grid, while keeping raw severity at "
        "the champion settings."
    ),
    "hypothesis": (
        "Mid-leaf frequency improved capped Gini with fold agreement, while "
        "the aggressive capped-severity run produced the highest mean capped "
        "Gini so far. Combining them may clear the segmentation Gini threshold, "
        "though it must still pass fold agreement and calibration gates."
    ),
    "actuarial_rationale": (
        "This is an intentionally aggressive segmentation-research test, not a "
        "pricing-level candidate. It is only acceptable if the ranking lift is "
        "broad across folds and the capped severity flexibility does not create "
        "unexplained instability."
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
                "num_leaves": 31,
                "min_data_in_leaf": 100,
                "learning_rate": 0.03,
                "feature_fraction": 0.8,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 31,
                "min_data_in_leaf": 75,
                "learning_rate": 0.025,
                "feature_fraction": 0.75,
                "bagging_fraction": 0.85,
                "lambda_l2": 15,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
