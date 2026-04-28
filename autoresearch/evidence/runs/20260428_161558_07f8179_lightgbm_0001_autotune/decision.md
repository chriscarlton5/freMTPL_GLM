# lightgbm_0001_autotune

## Hypothesis
Fine-tuning leaves from champion config.

## Candidate Change
Auto-generated: leaves variation on champion. FF=0.515, L2=13.4, leaves=18/26

## CV Metric Summary
- Capped pure premium Gini: 0.1898
- Capped pure premium calibration gap: -0.0096
- Capped pure premium MAE: 218.1095
- Raw pure premium Gini: 0.213
- Raw pure premium calibration gap: -0.0656
- Runtime seconds: 26.812802

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | True |
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
Testing leaves variation for potential improvement.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
