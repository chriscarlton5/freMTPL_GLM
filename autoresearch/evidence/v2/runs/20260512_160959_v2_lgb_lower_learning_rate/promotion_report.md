# V2 Promotion Report: v2_lgb_lower_learning_rate

## Decision

`research_only`

## Candidate

- Idea family: `model_structure`
- Parent: `lightgbm_regularized_challenger`
- Hypothesis: Use slower boosting to test whether smoother ensembles improve holdout capped Gini.
- Expected mechanism: Change regularization structure enough to test generalization, while staying close to the defensible initial GBM basin.
- Known tradeoff risk: May reduce useful segmentation by over-regularizing the already strong benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_lgb_lower_learning_rate` | candidate | 0.2102 | 0.3813 | 215.8488 | -0.0018 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.00182979404607568,
  "capped_pp_calibration_abs_deterioration": -0.00381246100341717,
  "capped_pp_mae_deterioration": 0.0016901942586839177,
  "capped_pp_rmse_deterioration": -1.5643991732019304e-05,
  "holdout_capped_pp_gini_gain": 0.002679120038979993,
  "holdout_raw_pp_gini_gain": -0.004686251301926958,
  "policy_leakage_count": 0
}
```

## Gate Failures

- raw PP Gini deteriorated beyond tolerance

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
