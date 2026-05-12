# lightgbm_0001_autotune

## Hypothesis
Fine-tuning lr from champion config.

## Candidate Change
Auto-generated: lr variation on champion. FF=0.515, L2=13.4, leaves=16/24

## CV Metric Summary
- Capped pure premium Gini: 0.1883
- Capped pure premium calibration gap: -0.0125
- Capped pure premium MAE: 217.812
- Raw pure premium Gini: 0.2079
- Raw pure premium calibration gap: -0.0654
- Runtime seconds: 26.034473

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Testing lr variation for potential improvement.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
