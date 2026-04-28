from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0005",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.536 L2=12.3",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 15,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5362463999415745,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 12.272785217300324
      },
      {
        "num_leaves": 23,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.48624639994157454,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 10.272785217300324
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5362463999415745,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 10.272785217300324
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48624639994157454,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 9.272785217300324
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5362463999415745,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 10.272785217300324
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.48624639994157454,
        "bagging_fraction": 0.5362463999415745,
        "lambda_l2": 9.272785217300324
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)