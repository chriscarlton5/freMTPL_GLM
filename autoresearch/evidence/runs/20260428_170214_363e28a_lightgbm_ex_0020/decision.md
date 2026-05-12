# lightgbm_ex_0020

## Hypothesis
Exploration: very_low_ff

## Candidate Change
Explore: very_low_ff. FF=0.457, L2=14.4, leaves=17

## CV Metric Summary
- Capped pure premium Gini: 0.1888
- Capped pure premium calibration gap: -0.0052
- Capped pure premium MAE: 218.6708
- Raw pure premium Gini: 0.211
- Raw pure premium calibration gap: -0.07
- Runtime seconds: 29.384008

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
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Breaking plateau with new direction

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
