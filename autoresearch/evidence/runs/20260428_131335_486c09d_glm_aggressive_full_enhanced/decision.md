# glm_aggressive_full_enhanced

## Hypothesis
Past GLM attempts tested one change at a time. LightGBM wins because it captures combined nonlinearities + interactions. This candidate tests that theory by combining spline flexibility with multiple interactions and calibration in one model.

## Candidate Change
GLM with max spline flexibility (df=5), multiple interactions (DriverAge:CarAge, Power:Brand), and component calibration scalars to test whether combining all terms outperforms the baseline.

## CV Metric Summary
- Capped pure premium Gini: 0.1641
- Capped pure premium calibration gap: 0.0286
- Capped pure premium MAE: 221.6971
- Raw pure premium Gini: 0.1587
- Raw pure premium calibration gap: 0.0995
- Runtime seconds: 137.766648

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | False |
| segmentation_capped_calibration_tolerance | True |
| segmentation_capped_mae_tolerance | False |
| segmentation_capped_rmse_tolerance | True |
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | False |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
All components are GLM with natural splines - fully transparent and defensible. Multiple interactions capture the interaction effects LightGBM discovered. Component scalars calibrate on training fold only to avoid leakage.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_capped_calibration_tight, pricing_capped_mae_tolerance, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_capped_mae_tolerance, segmentation_raw_gini_not_materially_worse

Log truncated: False
