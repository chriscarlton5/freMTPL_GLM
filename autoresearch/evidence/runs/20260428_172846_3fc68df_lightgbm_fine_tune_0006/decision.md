# lightgbm_fine_tune_0006

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.514 L2=12.7 L=18

## CV Metric Summary
- Capped pure premium Gini: 0.1852
- Capped pure premium calibration gap: -0.0196
- Capped pure premium MAE: 217.0589
- Raw pure premium Gini: 0.2119
- Raw pure premium calibration gap: -0.0729
- Runtime seconds: 29.881557

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
