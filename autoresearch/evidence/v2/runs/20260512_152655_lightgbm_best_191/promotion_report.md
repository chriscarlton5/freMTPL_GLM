# V2 Promotion Report: lightgbm_best_191

## Decision

`research_only`

## Candidate

- Idea family: `hyperparameter_tuning`
- Parent: `lightgbm_regularized_challenger`
- Hypothesis: Replay the v1 CV-selected autoresearch champion as a known non-promoted example for the v2 promotion gates.
- Expected mechanism: High randomization may improve repeated-CV ranking, but prior holdout evidence suggests it does not beat the initial regularized LightGBM on capped pure-premium Gini.
- Known tradeoff risk: May optimize repeated CV while failing blind holdout capped pure-premium Gini.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `lightgbm_best_191` | candidate | 0.2065 | 0.3879 | 215.0472 | -0.0099 | 0 | 0 |

## Promotion Deltas

```json
{
  "bad_prediction_count": 0,
  "candidate_abs_capped_pp_calibration_gap": 0.00991270838525616,
  "capped_pp_calibration_abs_deterioration": 0.00427045333576331,
  "capped_pp_mae_deterioration": -0.002029580077604758,
  "capped_pp_rmse_deterioration": 5.2217631406704744e-05,
  "holdout_capped_pp_gini_gain": -0.0010022855607610126,
  "holdout_raw_pp_gini_gain": 0.0018898569468620008,
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
