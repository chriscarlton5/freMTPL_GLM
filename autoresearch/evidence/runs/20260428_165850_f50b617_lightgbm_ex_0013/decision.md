# lightgbm_ex_0013

## Hypothesis
Exploration: different_l2

## Candidate Change
Explore: different_l2. FF=0.502, L2=9.7, leaves=16

## CV Metric Summary
- Capped pure premium Gini: 0.1846
- Capped pure premium calibration gap: -0.0205
- Capped pure premium MAE: 216.9756
- Raw pure premium Gini: 0.2153
- Raw pure premium calibration gap: -0.0648
- Runtime seconds: 27.91591

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
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Breaking plateau with new direction

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
