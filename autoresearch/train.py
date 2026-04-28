"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_midleaf_frequency_restrained_severity",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger adding one mid-leaf frequency option while "
        "restraining raw and capped severity grids to conservative leaf sizes."
    ),
    "hypothesis": (
        "The strongest near misses came from mid-leaf frequency lift plus "
        "capped-severity flexibility. Holding severity conservative may retain "
        "the frequency ranking signal while avoiding capped severity overfit."
    ),
    "actuarial_rationale": (
        "This is a segmentation research candidate, not a pricing-level model. "
        "It tests whether the incremental lift is coming from a plausible claim "
        "frequency segmentation signal rather than unstable severity slicing."
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
                "min_data_in_leaf": 900,
                "learning_rate": 0.035,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 300,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 7,
                "min_data_in_leaf": 500,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 20,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 300,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 7,
                "min_data_in_leaf": 500,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 20,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
