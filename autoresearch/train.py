"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "lightgbm_frequency_ranking_push",
    "is_baseline": False,
    "model_type": "lightgbm",
    "description": (
        "LightGBM challenger that keeps champion severity and capped severity "
        "settings while adding a more flexible, still regularized frequency "
        "option to test whether fold-balanced segmentation lift is frequency-led."
    ),
    "hypothesis": (
        "Prior capped-severity flexibility mainly helped fold 3. A controlled "
        "frequency-ranking push may improve capped pure premium Gini across at "
        "least two folds without worsening capped MAE or calibration."
    ),
    "actuarial_rationale": (
        "Frequency is generally the more stable component in MTPL pricing. This "
        "candidate keeps severity stable and limits the extra flexibility to one "
        "frequency-grid option with minimum leaf and L2 controls."
    ),
    "lightgbm": {
        "nrounds": 150,
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
                "num_leaves": 63,
                "min_data_in_leaf": 900,
                "learning_rate": 0.025,
                "feature_fraction": 0.8,
                "bagging_fraction": 0.85,
                "lambda_l2": 15,
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
        ],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
