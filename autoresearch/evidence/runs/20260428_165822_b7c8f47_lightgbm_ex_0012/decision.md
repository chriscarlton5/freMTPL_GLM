# lightgbm_ex_0012

## Hypothesis
Exploration: different_lr

## Candidate Change
Explore: different_lr. FF=0.511, L2=12.5, leaves=15

## CV Metric Summary
- Capped pure premium Gini: 0.1842
- Capped pure premium calibration gap: -0.0192
- Capped pure premium MAE: 217.1063
- Raw pure premium Gini: 0.2044
- Raw pure premium calibration gap: -0.0679
- Runtime seconds: 28.010693

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Breaking plateau with new direction

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
