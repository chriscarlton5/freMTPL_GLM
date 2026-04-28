# lightgbm_ex_0014

## Hypothesis
Exploration: balanced

## Candidate Change
Explore: balanced. FF=0.517, L2=11.4, leaves=18

## CV Metric Summary
- Capped pure premium Gini: 0.1869
- Capped pure premium calibration gap: -0.019
- Capped pure premium MAE: 217.0987
- Raw pure premium Gini: 0.2108
- Raw pure premium calibration gap: -0.0725
- Runtime seconds: 28.9376

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
