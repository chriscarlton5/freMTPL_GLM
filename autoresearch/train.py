"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_midleaf_stronger_capped_raw_severity_push",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger using the strongest mid-leaf frequency and "
        "stronger capped-severity near-miss grids, with an added raw-severity "
        "option for monitoring lift."
    ),
    "hypothesis": (
        "The best capped segmentation near miss already passes raw Gini "
        "monitoring. A slightly broader raw-severity grid may improve raw pure "
        "premium monitoring without changing the capped ranking path."
    ),
    "actuarial_rationale": (
        "This is segmentation research only. The raw-severity option is useful "
        "only if it improves monitoring without weakening capped stability."
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
            {
                "num_leaves": 31,
                "min_data_in_leaf": 100,
                "learning_rate": 0.025,
                "feature_fraction": 0.75,
                "bagging_fraction": 0.85,
                "lambda_l2": 15,
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
