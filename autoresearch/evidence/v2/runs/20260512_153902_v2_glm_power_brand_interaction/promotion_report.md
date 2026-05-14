# V2 Promotion Report: v2_glm_power_brand_interaction

## Decision

`research_only`

## Candidate

- Idea family: `transparent_glm`
- Parent: `baseline_enhanced_glm_splines`
- Hypothesis: Vehicle power by brand may capture stable vehicle-risk segmentation without GBM opacity.
- Expected mechanism: Replace local LightGBM tuning with stable, reviewable interactions across frequency and severity components.
- Known tradeoff risk: Transparent interactions may be too rigid or too parameter-heavy to beat the LightGBM benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_glm_power_brand_interaction` | candidate | 0.1912 | 0.3410 | 217.1469 | 0.0125 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.0125071994947424,
  "capped_pp_calibration_abs_deterioration": 0.00686494444524955,
  "capped_pp_mae_deterioration": 0.007714344726705081,
  "capped_pp_rmse_deterioration": 0.00012468841102541292,
  "holdout_capped_pp_gini_gain": -0.016308406516204993,
  "holdout_raw_pp_gini_gain": -0.04505360164455896,
  "policy_leakage_count": 0
}
```

## Gate Failures

- holdout capped PP Gini did not beat champion by required margin
- capped PP MAE deterioration exceeded tolerance
- capped PP calibration deterioration exceeded tolerance
- raw PP Gini deteriorated beyond tolerance

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
