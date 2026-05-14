# V2 Promotion Report: v2_glm_age_powerbrand

## Decision

`research_only`

## Candidate

- Idea family: `transparent_glm`
- Parent: `baseline_enhanced_glm_splines`
- Hypothesis: Combine the strongest transparent driver/vehicle structure with vehicle-type segmentation.
- Expected mechanism: Replace local LightGBM tuning with stable, reviewable interactions across frequency and severity components.
- Known tradeoff risk: Transparent interactions may be too rigid or too parameter-heavy to beat the LightGBM benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_glm_age_powerbrand` | candidate | 0.2001 | 0.3641 | 217.1781 | 0.0125 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.0125386327456107,
  "capped_pp_calibration_abs_deterioration": 0.006896377696117851,
  "capped_pp_mae_deterioration": 0.007859051857217823,
  "capped_pp_rmse_deterioration": 5.96683367793357e-05,
  "holdout_capped_pp_gini_gain": -0.007449622276464007,
  "holdout_raw_pp_gini_gain": -0.02189536563732497,
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
