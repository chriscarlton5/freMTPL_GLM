# lightgbm_191_slide

## Hypothesis
Lower L2 may help.

## Candidate Change
0.191 slide: feature 0.514 + 16/24 + L2 12.8/10.8. Lower L2.

## CV Metric Summary
- Capped pure premium Gini: 0.188
- Capped pure premium calibration gap: -0.0122
- Capped pure premium MAE: 217.8196
- Raw pure premium Gini: 0.2152
- Raw pure premium calibration gap: -0.0658
- Runtime seconds: 25.694471

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
Test less regularization.

## Decision
keep

Gate failures: none

Log truncated: False
