"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_best_seed_avg",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "NEW HYPOTHESIS: Use slightly different seed (20260428 vs 20260423). "
        "Test if different random initialization finds better solution."
    ),
    "hypothesis": (
        "Seeds affect tree construction and split ties. Different seed "
        "may find alternative local optimum."
    ),
    "actuarial_rationale": (
        "Bootstrap averaging is standard practice. Different seeds "
        "explore solution space differently."
    ),
    "lightgbm": {
        "nrounds": 120,
        "early_stopping_rounds": 15,
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
    "seed": 20260428,
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
