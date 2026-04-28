# lightgbm_ex_0019

## Hypothesis
Exploration: higher_ff

## Candidate Change
Explore: higher_ff. FF=0.527, L2=11.4, leaves=16

## CV Metric Summary
- Capped pure premium Gini: 0.1858
- Capped pure premium calibration gap: -0.0204
- Capped pure premium MAE: 216.9784
- Raw pure premium Gini: 0.2052
- Raw pure premium calibration gap: -0.0775
- Runtime seconds: 28.253444

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Breaking plateau with new direction

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
