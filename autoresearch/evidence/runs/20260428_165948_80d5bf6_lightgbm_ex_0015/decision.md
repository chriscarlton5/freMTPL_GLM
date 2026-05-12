# lightgbm_ex_0015

## Hypothesis
Exploration: fewer_leaves

## Candidate Change
Explore: fewer_leaves. FF=0.502, L2=12.5, leaves=12

## CV Metric Summary
- Capped pure premium Gini: 0.1823
- Capped pure premium calibration gap: -0.023
- Capped pure premium MAE: 216.7092
- Raw pure premium Gini: 0.2162
- Raw pure premium calibration gap: -0.0647
- Runtime seconds: 27.749799

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Breaking plateau with new direction

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
