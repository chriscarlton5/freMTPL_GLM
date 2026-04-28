# lightgbm_smoother_more_reg

## Hypothesis
Higher L2 reduces variance from aggressive fits. May find more generalizable solution while keeping high Gini.

## Candidate Change
NEW HYPOTHESIS: Strengthen L2 regularization (12-15 vs 8-10) to reduce variance. Previous run hit 0.1862 but high MAE - overfitting.

## CV Metric Summary
- Capped pure premium Gini: 0.1847
- Capped pure premium calibration gap: -0.0106
- Capped pure premium MAE: 217.982
- Raw pure premium Gini: 0.2003
- Raw pure premium calibration gap: -0.0436
- Runtime seconds: 18.4993

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
More regularization = more stable. Keep predictions for pricing.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
