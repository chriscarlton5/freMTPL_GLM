# lightgbm_fine_tune_0005

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.513 L2=13.4 L=16

## CV Metric Summary
- Capped pure premium Gini: 0.1852
- Capped pure premium calibration gap: -0.0203
- Capped pure premium MAE: 216.9948
- Raw pure premium Gini: 0.213
- Raw pure premium calibration gap: -0.073
- Runtime seconds: 29.527297

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
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Autonomous research

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
