"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_dart_booster",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "NEW HYPOTHESIS: Use DART booster ( dropout + tree) instead of GBDT. "
        "Drops trees during training to reduce overfitting."
    ),
    "hypothesis": (
        "DART applies dropout to trees - prevents overfitting from greedy trees. "
        "Different optimization path may find new local optimum."
    ),
    "actuarial_rationale": (
        "DART is alternative boosting method. Has different bias-variance tradeoff. "
        "Sometimes finds better solutions than GBDT."
    ),
    "lightgbm": {
        "nrounds": 120,
        "early_stopping_rounds": 15,
        "boosting_type": "dart",
        "drop_rate": 0.1,
        "skip_drop": 0.5,
        "frequency_grid": [
            {
                "num_leaves": 15,
                "min_data_in_leaf": 1600,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 10,
            },
            {
                "num_leaves": 24,
                "min_data_in_leaf": 1300,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
        ],
        "severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 190,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 150,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
        "capped_severity_grid": [
            {
                "num_leaves": 7,
                "min_data_in_leaf": 190,
                "learning_rate": 0.04,
                "feature_fraction": 0.87,
                "bagging_fraction": 0.87,
                "lambda_l2": 8,
            },
            {
                "num_leaves": 11,
                "min_data_in_leaf": 150,
                "learning_rate": 0.035,
                "feature_fraction": 0.82,
                "bagging_fraction": 0.87,
                "lambda_l2": 6,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
