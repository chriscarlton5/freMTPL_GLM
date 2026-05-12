# lightgbm_aggressive_capped_severity

## Hypothesis
The previous capped-severity-only variant improved capped Gini but not enough to pass the champion gate. A stronger capped-severity search may extract additional stable segmentation signal.

## Candidate Change
LightGBM challenger that preserves the current frequency and raw severity grids while testing a more aggressive capped-severity grid.

## CV Metric Summary
- Capped pure premium Gini: 0.1856
- Capped pure premium calibration gap: -0.0256
- Capped pure premium MAE: 216.3984
- Raw pure premium Gini: 0.2
- Raw pure premium calibration gap: -0.0465
- Runtime seconds: 25.542571

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| minimum_capped_gini_gain | False |
| minimum_fold_agreement | False |
| capped_calibration_tolerance | True |
| capped_mae_tolerance | True |
| capped_rmse_tolerance | True |
| raw_gini_not_materially_worse | True |

## Actuarial Interpretation
This intentionally concentrates extra flexibility in capped severity, the stable severity target, while preserving the existing frequency and raw severity settings. It must still pass calibration and fold gates.

## Decision
discard

Gate failures: minimum_capped_gini_gain, minimum_fold_agreement

Log truncated: False
