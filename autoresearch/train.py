"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_aggressive_capped_severity",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger that preserves the current frequency and raw "
        "severity grids while testing a more aggressive capped-severity grid."
    ),
    "hypothesis": (
        "The previous capped-severity-only variant improved capped Gini but not "
        "enough to pass the champion gate. A stronger capped-severity search may "
        "extract additional stable segmentation signal."
    ),
    "actuarial_rationale": (
        "This intentionally concentrates extra flexibility in capped severity, "
        "the stable severity target, while preserving the existing frequency and "
        "raw severity settings. It must still pass calibration and fold gates."
    ),
    "lightgbm": {
        "nrounds": 180,
        "early_stopping_rounds": 25,
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
                "num_leaves": 63,
                "min_data_in_leaf": 80,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 3,
            },
            {
                "num_leaves": 127,
                "min_data_in_leaf": 100,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
