from prepare import run_experiment
CANDIDATE = {
  "id": "lightgbm_ex_0028",
  "is_baseline": False,
  "model_type": "lightgbm",
  "description": "ex: FF=0.498 L2=11.3",
  "hypothesis": "ex",
  "actuarial_rationale": "auto",
  "lightgbm": {
    "nrounds": 175,
    "early_stopping_rounds": 22,
    "frequency_grid": [
      {
        "num_leaves": 16,
        "min_data_in_leaf": 1700,
        "learning_rate": 0.036,
        "feature_fraction": 0.4976250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 11.343983263992817
      },
      {
        "num_leaves": 24,
        "min_data_in_leaf": 1400,
        "learning_rate": 0.031,
        "feature_fraction": 0.4476250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 9.343983263992817
      }
    ],
    "severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4976250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 9.343983263992817
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4476250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 8.343983263992817
      }
    ],
    "capped_severity_grid": [
      {
        "num_leaves": 7,
        "min_data_in_leaf": 200,
        "learning_rate": 0.036,
        "feature_fraction": 0.4976250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 9.343983263992817
      },
      {
        "num_leaves": 11,
        "min_data_in_leaf": 150,
        "learning_rate": 0.031,
        "feature_fraction": 0.4476250933210028,
        "bagging_fraction": 0.4976250933210028,
        "lambda_l2": 8.343983263992817
      }
    ]
  }
}
if __name__ == "__main__": run_experiment(CANDIDATE)
