# lightgbm_ex_0018

## Hypothesis
Exploration: more_leaves

## Candidate Change
Explore: more_leaves. FF=0.519, L2=12.4, leaves=24

## CV Metric Summary
- Capped pure premium Gini: 0.1892
- Capped pure premium calibration gap: -0.0124
- Capped pure premium MAE: 217.7865
- Raw pure premium Gini: 0.2118
- Raw pure premium calibration gap: -0.0684
- Runtime seconds: 29.543005

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
