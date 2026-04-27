# enhanced_glm_component_scalars

## Hypothesis
Fold-internal component calibration can improve loss-cost level while preserving the enhanced GLM's transparent segmentation structure.

## Candidate Change
Baseline transparent enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds component-level frequency, raw severity, and capped severity calibration scalars estimated only inside each training fold.

## CV Metric Summary
- Capped pure premium Gini: 0.1666
- Capped pure premium calibration gap: 0.0326
- Capped pure premium MAE: 222.1188
- Raw pure premium Gini: 0.1467
- Raw pure premium calibration gap: 0.1071
- Runtime seconds: 18.569719

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| minimum_capped_gini_gain | False |
| minimum_fold_agreement | True |
| capped_calibration_tolerance | False |
| capped_mae_tolerance | False |
| capped_rmse_tolerance | True |
| raw_gini_not_materially_worse | False |

## Actuarial Interpretation
Component scalars are easy to audit and separate frequency, raw severity, and capped severity bias. They should only be retained if they improve calibration without weakening capped pure premium lift or stability.

## Decision
discard

Gate failures: minimum_capped_gini_gain, capped_calibration_tolerance, capped_mae_tolerance, raw_gini_not_materially_worse

Log truncated: False
