# lightgbm_ex_0012

## Hypothesis
ex

## Candidate Change
ex: FF=0.495 L2=11.1

## CV Metric Summary
- Capped pure premium Gini: 0.1887
- Capped pure premium calibration gap: -0.0198
- Capped pure premium MAE: 217.0982
- Raw pure premium Gini: 0.2151
- Raw pure premium calibration gap: -0.0713
- Runtime seconds: 29.949698

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
