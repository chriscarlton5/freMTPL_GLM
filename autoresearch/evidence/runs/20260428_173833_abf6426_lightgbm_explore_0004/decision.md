# lightgbm_explore_0004

## Hypothesis
EXPLORE approach

## Candidate Change
EXPLORE: FF=0.520 L2=13.2 L=17

## CV Metric Summary
- Capped pure premium Gini: 0.1874
- Capped pure premium calibration gap: -0.0134
- Capped pure premium MAE: 217.6972
- Raw pure premium Gini: 0.2057
- Raw pure premium calibration gap: -0.0684
- Runtime seconds: 29.600021

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Autonomous research

## Decision
keep

Gate failures: none

Log truncated: False
