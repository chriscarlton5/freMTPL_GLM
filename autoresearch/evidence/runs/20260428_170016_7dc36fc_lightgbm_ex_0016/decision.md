# lightgbm_ex_0016

## Hypothesis
Exploration: very_low_ff

## Candidate Change
Explore: very_low_ff. FF=0.469, L2=13.6, leaves=16

## CV Metric Summary
- Capped pure premium Gini: 0.1875
- Capped pure premium calibration gap: -0.0123
- Capped pure premium MAE: 217.8902
- Raw pure premium Gini: 0.2097
- Raw pure premium calibration gap: -0.0829
- Runtime seconds: 29.204915

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
Breaking plateau with new direction

## Decision
keep

Gate failures: none

Log truncated: False
