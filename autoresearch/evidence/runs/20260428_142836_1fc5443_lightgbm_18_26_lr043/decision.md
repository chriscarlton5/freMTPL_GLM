# lightgbm_18_26_lr043

## Hypothesis
More leaves + moderate LR.

## Candidate Change
18/26 leaves, 0.043 LR, lower L2 (7-8). More trees.

## CV Metric Summary
- Capped pure premium Gini: 0.1833
- Capped pure premium calibration gap: -0.0125
- Capped pure premium MAE: 217.7263
- Raw pure premium Gini: 0.197
- Raw pure premium calibration gap: -0.0471
- Runtime seconds: 20.18221

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
Alternative exploration.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
