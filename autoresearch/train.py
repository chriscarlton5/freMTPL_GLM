from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0001",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "EXPLORE: FF=0.494, L2=13.9, leaves=17",
  "hypothesis": "EXPLORE approach",
  "actuarial_rationale": "Autonomous exploration",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 17,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4938731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 13.863769311628491
      },
      {
        "num_leaves": 25,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4438731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 11.863769311628491
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4938731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 11.863769311628491
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4438731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 10.863769311628491
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4938731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 11.863769311628491
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4438731933735759,
        "bagging_fraction": 0.4938731933735759,
        "lambda_l2": 10.863769311628491
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)