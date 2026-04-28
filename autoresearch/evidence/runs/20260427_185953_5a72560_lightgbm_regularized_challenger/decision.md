# lightgbm_regularized_challenger

## Hypothesis
A constrained LightGBM may improve capped pure premium ranking enough to qualify as a segmentation/research champion while preserving capped calibration and error stability.

## Candidate Change
Regularized LightGBM challenger using constrained leaf counts and moderate L2 penalties for frequency, raw severity, and capped severity.

## CV Metric Summary
- Capped pure premium Gini: 0.1827
- Capped pure premium calibration gap: -0.0145
- Capped pure premium MAE: 217.6245
- Raw pure premium Gini: 0.198
- Raw pure premium calibration gap: -0.0471
- Runtime seconds: 20.15359

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| minimum_capped_gini_gain | True |
| minimum_fold_agreement | True |
| capped_calibration_tolerance | True |
| capped_mae_tolerance | True |
| capped_rmse_tolerance | True |
| raw_gini_not_materially_worse | True |

## Actuarial Interpretation
The existing report showed LightGBM can find segmentation signal, but it is not accepted as a pricing level unless calibration and stability also pass. This candidate intentionally limits flexibility to avoid a black-box gift.

## Decision
keep

Gate failures: none

Log truncated: False
