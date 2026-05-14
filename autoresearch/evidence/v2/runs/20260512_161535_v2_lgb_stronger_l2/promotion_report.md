# V2 Promotion Report: v2_lgb_stronger_l2

## Decision

`promote`

## Candidate

- Idea family: `stability`
- Parent: `lightgbm_regularized_challenger`
- Hypothesis: Increase L2 penalties to test whether the benchmark can be stabilized without losing ranking.
- Expected mechanism: Change regularization structure enough to test generalization, while staying close to the defensible initial GBM basin.
- Known tradeoff risk: May reduce useful segmentation by over-regularizing the already strong benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_lgb_stronger_l2` | candidate | 0.2089 | 0.3858 | 215.5038 | -0.0054 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.00543439777465492,
  "capped_pp_calibration_abs_deterioration": -0.00020785727483792985,
  "capped_pp_mae_deterioration": 8.913046214600775e-05,
  "capped_pp_rmse_deterioration": -9.410383593263973e-06,
  "holdout_capped_pp_gini_gain": 0.0013807970999079877,
  "holdout_raw_pp_gini_gain": -0.00021484699488000247,
  "policy_leakage_count": 0
}
```

## Gate Failures

none

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
