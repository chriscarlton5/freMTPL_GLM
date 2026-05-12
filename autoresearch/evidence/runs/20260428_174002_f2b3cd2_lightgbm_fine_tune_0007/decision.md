# lightgbm_fine_tune_0007

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.511 L2=13.1 L=16

## CV Metric Summary
- Capped pure premium Gini: 0.1868
- Capped pure premium calibration gap: -0.0206
- Capped pure premium MAE: 216.9767
- Raw pure premium Gini: 0.2128
- Raw pure premium calibration gap: -0.0723
- Runtime seconds: 28.796175

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
