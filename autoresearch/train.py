"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_midleaf_frequency_mild_capped",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger combining the mid-leaf frequency probe with one "
        "mild capped-severity option while retaining all champion grid options."
    ),
    "hypothesis": (
        "The mid-leaf frequency option passed fold agreement but missed the "
        "minimum Gini gain. Adding a mild capped-severity option may provide "
        "enough additional capped pure premium lift while preserving the fold "
        "agreement and MAE improvements."
    ),
    "actuarial_rationale": (
        "This combines two near-miss ideas sparingly. Frequency remains the "
        "primary stable signal, while capped severity gets only one additional "
        "regularized option rather than another broad severity search."
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
                "min_data_in_leaf": 200,
                "learning_rate": 0.025,
                "feature_fraction": 0.85,
                "bagging_fraction": 0.9,
                "lambda_l2": 15,
            },
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
