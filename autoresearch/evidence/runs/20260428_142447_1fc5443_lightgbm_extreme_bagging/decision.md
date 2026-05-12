# lightgbm_extreme_bagging

## Hypothesis
More randomness may find better solutions.

## Candidate Change
NEW: High bagging fraction (0.92) more randomness, lower feature fraction (0.75). Maximum diversity approach.

## CV Metric Summary
- Capped pure premium Gini: 0.1817
- Capped pure premium calibration gap: -0.0143
- Capped pure premium MAE: 217.6175
- Raw pure premium Gini: 0.1997
- Raw pure premium calibration gap: -0.0359
- Runtime seconds: 19.197078

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
Diversity exploration.

## Decision
keep

Gate failures: none

Log truncated: False
