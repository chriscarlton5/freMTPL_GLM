"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_deeper_frequency_capped",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger with slightly deeper frequency and capped-severity "
        "trees, retaining L2 regularization and minimum leaf-size controls."
    ),
    "hypothesis": (
        "The current LightGBM champion may be underfitting capped pure-premium "
        "ranking; modestly deeper trees may improve segmentation while staying "
        "inside the capped calibration and error gates."
    ),
    "actuarial_rationale": (
        "This remains a research-champion candidate, not an automatic pricing "
        "level. The depth increase is deliberately modest and still constrained "
        "by minimum leaf sizes and L2 penalties."
    ),
    "lightgbm": {
        "nrounds": 160,
        "early_stopping_rounds": 20,
        "frequency_grid": [
            {
                "num_leaves": 31,
                "min_data_in_leaf": 900,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
            {
                "num_leaves": 63,
                "min_data_in_leaf": 1200,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 12,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 15,
                "min_data_in_leaf": 150,
                "learning_rate": 0.04,
                "feature_fraction": 0.9,
                "bagging_fraction": 0.9,
                "lambda_l2": 5,
            },
            {
                "num_leaves": 31,
                "min_data_in_leaf": 250,
                "learning_rate": 0.03,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 12,
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
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
