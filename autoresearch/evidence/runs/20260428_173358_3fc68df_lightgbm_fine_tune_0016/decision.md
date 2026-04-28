# lightgbm_fine_tune_0016

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.522 L2=12.8 L=14

## CV Metric Summary
- Capped pure premium Gini: 0.1857
- Capped pure premium calibration gap: -0.0148
- Capped pure premium MAE: 217.56
- Raw pure premium Gini: 0.2122
- Raw pure premium calibration gap: -0.066
- Runtime seconds: 30.124782

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
Autonomous research

## Decision
keep

Gate failures: none

Log truncated: False
