from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ft_0021",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ft: FF=0.516 L2=13.3",
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
        "feature_fraction": 0.5156083768382798,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 13.328510002048125
      },
      {
        "num_leaves": 26,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.46560837683827977,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 11.328510002048125
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5156083768382798,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 11.328510002048125
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46560837683827977,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 10.328510002048125
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.5156083768382798,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 11.328510002048125
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.46560837683827977,
        "bagging_fraction": 0.5156083768382798,
        "lambda_l2": 10.328510002048125
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)