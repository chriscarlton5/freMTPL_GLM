from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_explore_0017",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "EXPLORE: FF=0.528 L2=13.5 L=20",
  "hypothesis": "EXPLORE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 20,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5278135024711896,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 13.545551284042663
      },
      {
        "num_leaves": 28,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.47781350247118964,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 11.545551284042663
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5278135024711896,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 11.545551284042663
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.47781350247118964,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 10.545551284042663
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5278135024711896,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 11.545551284042663
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.47781350247118964,
        "bagging_fraction": 0.5278135024711896,
        "lambda_l2": 10.545551284042663
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)