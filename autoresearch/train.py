from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0026",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.516 L2=13.4",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5160173030980246,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 13.385312345706728
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46601730309802464,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 11.385312345706728
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5160173030980246,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 11.385312345706728
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46601730309802464,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 10.385312345706728
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5160173030980246,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 11.385312345706728
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46601730309802464,
        "bagging_fraction": 0.5160173030980246,
        "lambda_l2": 10.385312345706728
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
