from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ps_0003",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ps: FF=0.509 L2=16.4",
  "hypothesis": "ps",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 19,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5094727866915792,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 16.358227418618455
      },
      {
        "num_leaves": 27,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.45947278669157926,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 14.358227418618455
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5094727866915792,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 14.358227418618455
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45947278669157926,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 13.358227418618455
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5094727866915792,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 14.358227418618455
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.45947278669157926,
        "bagging_fraction": 0.5094727866915792,
        "lambda_l2": 13.358227418618455
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
