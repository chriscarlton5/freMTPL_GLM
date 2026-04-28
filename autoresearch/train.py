"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_expanded_regularized_grid",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "Regularized LightGBM challenger with an expanded inner-validation "
        "grid. It keeps the current champion settings available while adding "
        "more conservative frequency options and previously useful capped "
        "severity options."
    ),
    "hypothesis": (
        "The aggressive capped-severity run improved fold 3 but hurt folds 1 "
        "and 2. Keeping champion options in the grid while adding conservative "
        "alternatives may allow fold-specific inner validation to improve capped "
        "pure premium Gini without sacrificing fold agreement."
    ),
    "actuarial_rationale": (
        "This remains a segmentation/research candidate only. The broader grid "
        "is still constrained by minimum leaf sizes, feature/bagging fractions, "
        "and L2 regularization so that any gain is less likely to be a sparse "
        "black-box artifact."
    ),
    "lightgbm": {
        "nrounds": 160,
        "early_stopping_rounds": 20,
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
                "num_leaves": 15,
                "min_data_in_leaf": 2000,
                "learning_rate": 0.025,
                "feature_fraction": 0.8,
                "bagging_fraction": 0.85,
                "lambda_l2": 20,
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
                "num_leaves": 7,
                "min_data_in_leaf": 300,
                "learning_rate": 0.025,
                "feature_fraction": 0.8,
                "bagging_fraction": 0.85,
                "lambda_l2": 20,
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
                "min_data_in_leaf": 150,
                "learning_rate": 0.025,
                "feature_fraction": 0.8,
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
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
