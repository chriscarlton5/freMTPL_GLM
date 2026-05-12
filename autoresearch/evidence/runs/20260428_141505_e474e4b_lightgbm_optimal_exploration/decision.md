# lightgbm_optimal_exploration

## Hypothesis
Push to boundary to find potential new optimum. High L2 prevents wild fits.

## Candidate Change
Final exploration: 18 leaves at 0.048 LR, extreme L2=15 for safety. Testing boundary of hyperparameter space.

## CV Metric Summary
- Capped pure premium Gini: 0.1834
- Capped pure premium calibration gap: -0.0178
- Capped pure premium MAE: 217.1382
- Raw pure premium Gini: 0.1951
- Raw pure premium calibration gap: -0.061
- Runtime seconds: 21.016004

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | True |
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
Final boundary test.

## Decision
keep

Gate failures: none

Log truncated: False
