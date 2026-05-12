# lightgbm_fine_tune_0017

## Hypothesis
FINE_TUNE approach

## Candidate Change
FINE_TUNE: FF=0.521 L2=13.3 L=16

## CV Metric Summary
- Capped pure premium Gini: 0.1877
- Capped pure premium calibration gap: -0.0112
- Capped pure premium MAE: 217.922
- Raw pure premium Gini: 0.2083
- Raw pure premium calibration gap: -0.0758
- Runtime seconds: 32.608118

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
