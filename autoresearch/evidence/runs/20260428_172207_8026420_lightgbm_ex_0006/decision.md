# lightgbm_ex_0006

## Hypothesis
EXPLORE approach

## Candidate Change
EXPLORE: FF=0.482, L2=11.2, leaves=19

## CV Metric Summary
- Capped pure premium Gini: 0.1853
- Capped pure premium calibration gap: -0.0208
- Capped pure premium MAE: 216.9979
- Raw pure premium Gini: 0.2124
- Raw pure premium calibration gap: -0.0764
- Runtime seconds: 31.211044

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
Autonomous exploration

## Decision
keep

Gate failures: none

Log truncated: False
