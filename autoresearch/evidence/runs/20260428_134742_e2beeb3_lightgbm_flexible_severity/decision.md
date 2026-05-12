# lightgbm_flexible_severity

## Hypothesis
Frequency is optimized. Try more flexible severity to see if better severity estimation translates to better pure premium.

## Candidate Change
Best run: Gini 0.1851, calibration -0.98%. Now tune severity - more leaves (8-12 vs 7-11) for better severity estimation.

## CV Metric Summary
- Capped pure premium Gini: 0.1829
- Capped pure premium calibration gap: -0.0175
- Capped pure premium MAE: 217.2693
- Raw pure premium Gini: 0.1967
- Raw pure premium calibration gap: -0.0653
- Runtime seconds: 19.481369

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | False |
| segmentation_capped_calibration_tolerance | True |
| segmentation_capped_mae_tolerance | True |
| segmentation_capped_rmse_tolerance | True |
| segmentation_raw_gini_not_materially_worse | True |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Severity has high variance - try more flexible estimation while keeping frequency regularized.

## Decision
keep

Gate failures: none

Log truncated: False
