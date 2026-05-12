# lightgbm_ex_0009

## Hypothesis
Exploration: different_lr

## Candidate Change
Explore: different_lr. FF=0.520, L2=13.3, leaves=15

## CV Metric Summary
- Capped pure premium Gini: 0.1876
- Capped pure premium calibration gap: -0.0127
- Capped pure premium MAE: 217.777
- Raw pure premium Gini: 0.2121
- Raw pure premium calibration gap: -0.0663
- Runtime seconds: 27.81168

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
