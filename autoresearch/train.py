from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0031",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.517 L2=12.8",
  "hypothesis": "ft",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 18,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.517191645336387,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 12.843327027398956
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46719164533638696,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 10.843327027398956
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.517191645336387,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 10.843327027398956
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46719164533638696,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 9.843327027398956
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.517191645336387,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 10.843327027398956
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46719164533638696,
        "bagging_fraction": 0.517191645336387,
        "lambda_l2": 9.843327027398956
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
