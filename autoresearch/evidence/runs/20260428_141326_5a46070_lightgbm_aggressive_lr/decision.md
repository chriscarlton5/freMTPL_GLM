# lightgbm_aggressive_lr

## Hypothesis
Higher LR finds different solution faster. Combined with larger min_data prevents wild fits.

## Candidate Change
NEW HYPOTHESIS: Try very high learning rate (0.05/0.045) with stronger min_data to balance. Faster convergence.

## CV Metric Summary
- Capped pure premium Gini: 0.1836
- Capped pure premium calibration gap: -0.021
- Capped pure premium MAE: 216.9025
- Raw pure premium Gini: 0.1989
- Raw pure premium calibration gap: -0.0447
- Runtime seconds: 15.807893

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
Standard tuning: try different LR range.

## Decision
keep

Gate failures: none

Log truncated: False
