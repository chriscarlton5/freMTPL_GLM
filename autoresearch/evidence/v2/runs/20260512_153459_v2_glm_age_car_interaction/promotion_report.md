# V2 Promotion Report: v2_glm_age_car_interaction

## Decision

`research_only`

## Candidate

- Idea family: `transparent_glm`
- Parent: `baseline_enhanced_glm_splines`
- Hypothesis: Driver age and vehicle age may interact in a stable, actuarially explainable way.
- Expected mechanism: Replace local LightGBM tuning with stable, reviewable interactions across frequency and severity components.
- Known tradeoff risk: Transparent interactions may be too rigid or too parameter-heavy to beat the LightGBM benchmark.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `v2_glm_age_car_interaction` | candidate | 0.2101 | 0.3728 | 217.0748 | 0.0117 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.0117357601581656,
  "capped_pp_calibration_abs_deterioration": 0.00609350510867275,
  "capped_pp_mae_deterioration": 0.007379724222532174,
  "capped_pp_rmse_deterioration": -5.667816549036109e-05,
  "holdout_capped_pp_gini_gain": 0.0025947771582799928,
  "holdout_raw_pp_gini_gain": -0.01325752383238199,
  "policy_leakage_count": 0
}
```

## Gate Failures

- capped PP MAE deterioration exceeded tolerance
- capped PP calibration deterioration exceeded tolerance
- raw PP Gini deteriorated beyond tolerance

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
