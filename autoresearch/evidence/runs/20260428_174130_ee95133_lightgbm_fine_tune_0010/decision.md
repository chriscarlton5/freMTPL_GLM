# lightgbm_fine_tune_0010

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.513 L2=12.7 L=17

## CV Metric Summary
- Capped pure premium Gini: 0.1853
- Capped pure premium calibration gap: -0.0203
- Capped pure premium MAE: 216.9853
- Raw pure premium Gini: 0.2139
- Raw pure premium calibration gap: -0.0735
- Runtime seconds: 28.865976

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
Autonomous research

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
