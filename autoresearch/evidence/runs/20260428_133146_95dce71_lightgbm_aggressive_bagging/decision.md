# lightgbm_aggressive_bagging

## Hypothesis
More aggressive bagging + feature sampling adds diversity. Often improves generalization. Earlier runs showed ~0.184-0.185 range.

## Candidate Change
LightGBM with more aggressive bagging (0.92) and slight feature sampling to introduce more randomness, prevent correlated trees.

## CV Metric Summary
- Capped pure premium Gini: 0.1823
- Capped pure premium calibration gap: -0.0103
- Capped pure premium MAE: 218.0764
- Raw pure premium Gini: 0.1935
- Raw pure premium calibration gap: -0.0482
- Runtime seconds: 18.938643

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Bagging is standard ensemble technique - reduces variance. Combined with L2 regularization maintains defensibility.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
