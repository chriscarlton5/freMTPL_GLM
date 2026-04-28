from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_fine_tune_0018",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "FINE_TUNE: FF=0.512 L2=13.0 L=17",
  "hypothesis": "FINE_TUNE approach",
  "actuarial_rationale": "Autonomous research",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.5119597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 12.984947533209732
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 10.984947533209732
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5119597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 10.984947533209732
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 9.984947533209732
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5119597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 10.984947533209732
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4619597776416085,
        "bagging_fraction": 0.5119597776416085,
        "lambda_l2": 9.984947533209732
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)