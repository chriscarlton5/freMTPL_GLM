# V2 Promotion Report: lightgbm_regularized_challenger

## Decision

`current_champion`

## Candidate

- Idea family: `model_structure`
- Parent: `None`
- Hypothesis: The initial constrained LightGBM remains the current pricing champion and should be the benchmark every v2 candidate must beat.
- Expected mechanism: Constrained leaves, moderate L2 regularization, and high feature/bagging fractions preserve capped pure-premium ranking without excessive validation overfit.
- Known tradeoff risk: This is the current benchmark, not an attempted improvement.

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | benchmark | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `lightgbm_regularized_challenger` | candidate | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |

## Promotion Deltas

```json
{
  "current_champion": true
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
