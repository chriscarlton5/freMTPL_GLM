# V2 Promotion Report: v2_lgb_conservative_feature_fraction

## Decision

`research_only`

## Candidate

- Idea family: `stability`
- Parent: `lightgbm_regularized_challenger`
- Hypothesis: Moderate feature/bagging randomness without entering the failed best_191 low-fraction basin.
- Expected mechanism: Change regularization structure enough to test generalization, while staying close to the defensible initial GBM basin.
- Known tradeoff risk: May reduce useful segmentation by over-regularizing the already strong benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_lgb_conservative_feature_fraction` | candidate | 0.2019 | 0.3801 | 215.6822 | -0.0036 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.00357021455114244,
  "capped_pp_calibration_abs_deterioration": -0.00207204049835041,
  "capped_pp_mae_deterioration": 0.0009170662606074796,
  "capped_pp_rmse_deterioration": 5.3080604093813934e-06,
  "holdout_capped_pp_gini_gain": -0.005607189506066007,
  "holdout_raw_pp_gini_gain": -0.0059163772659029945,
  "policy_leakage_count": 0
}
```

## Gate Failures

- holdout capped PP Gini did not beat champion by required margin
- raw PP Gini deteriorated beyond tolerance

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
