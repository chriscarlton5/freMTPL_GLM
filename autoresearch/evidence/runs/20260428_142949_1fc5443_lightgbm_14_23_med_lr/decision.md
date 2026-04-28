# lightgbm_14_23_med_lr

## Hypothesis
Medium complexity + higher LR.

## Candidate Change
14/23 leaves, 0.045 LR, medium L2. Alternative.

## CV Metric Summary
- Capped pure premium Gini: 0.1828
- Capped pure premium calibration gap: -0.0147
- Capped pure premium MAE: 217.5189
- Raw pure premium Gini: 0.1991
- Raw pure premium calibration gap: -0.0448
- Runtime seconds: 18.359994

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Different balance.

## Decision
keep

Gate failures: none

Log truncated: False
