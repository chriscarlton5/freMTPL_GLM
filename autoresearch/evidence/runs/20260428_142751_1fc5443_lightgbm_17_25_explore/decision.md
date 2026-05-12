# lightgbm_17_25_explore

## Hypothesis
Different leaf combination.

## Candidate Change
17/25 leaves, 0.042 LR, 11 L2. Different from 15/24.

## CV Metric Summary
- Capped pure premium Gini: 0.1838
- Capped pure premium calibration gap: -0.0109
- Capped pure premium MAE: 217.9295
- Raw pure premium Gini: 0.1941
- Raw pure premium calibration gap: -0.0511
- Runtime seconds: 20.168917

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
Alternative config.

## Decision
keep

Gate failures: none

Log truncated: False
