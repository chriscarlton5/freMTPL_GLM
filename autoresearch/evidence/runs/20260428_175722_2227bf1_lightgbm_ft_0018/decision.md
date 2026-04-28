# lightgbm_ft_0018

## Hypothesis
ft

## Candidate Change
ft: FF=0.514 L2=12.9

## CV Metric Summary
- Capped pure premium Gini: 0.1832
- Capped pure premium calibration gap: -0.0203
- Capped pure premium MAE: 217.0044
- Raw pure premium Gini: 0.2124
- Raw pure premium calibration gap: -0.0727
- Runtime seconds: 28.373432

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
auto

## Decision
keep

Gate failures: none

Log truncated: False
