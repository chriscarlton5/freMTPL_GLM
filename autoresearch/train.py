from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0018",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.523 L2=13.3",
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
        "feature_fraction": 0.5227771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 13.300991987769656
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 11.300991987769656
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5227771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 11.300991987769656
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 10.300991987769656
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5227771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 11.300991987769656
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4727771390327304,
        "bagging_fraction": 0.5227771390327304,
        "lambda_l2": 10.300991987769656
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
