# V2 Promotion Report: v2_lgb_higher_leaf_floor

## Decision

`research_only`

## Candidate

- Idea family: `model_structure`
- Parent: `lightgbm_regularized_challenger`
- Hypothesis: Raise leaf floors to reduce variance while preserving the initial LightGBM structure.
- Expected mechanism: Change regularization structure enough to test generalization, while staying close to the defensible initial GBM basin.
- Known tradeoff risk: May reduce useful segmentation by over-regularizing the already strong benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_lgb_higher_leaf_floor` | candidate | 0.2065 | 0.3882 | 215.0479 | -0.0098 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.00978498398364084,
  "capped_pp_calibration_abs_deterioration": 0.00414272893414799,
  "capped_pp_mae_deterioration": -0.002026492155514739,
  "capped_pp_rmse_deterioration": -1.0234598535301541e-05,
  "holdout_capped_pp_gini_gain": -0.0010568869173800122,
  "holdout_raw_pp_gini_gain": 0.0021996859606400188,
  "policy_leakage_count": 0
}
```

## Gate Failures

- holdout capped PP Gini did not beat champion by required margin

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
