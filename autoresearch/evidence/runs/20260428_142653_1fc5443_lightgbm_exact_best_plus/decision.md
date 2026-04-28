# lightgbm_exact_best_plus

## Hypothesis
Tiny variations explore near-optimal space.

## Candidate Change
Exact best config with tiny variation: leaves 16/25, LR 0.041/0.036. Slight variation from 15/24 0.04/0.035.

## CV Metric Summary
- Capped pure premium Gini: 0.1829
- Capped pure premium calibration gap: -0.014
- Capped pure premium MAE: 217.5923
- Raw pure premium Gini: 0.1928
- Raw pure premium calibration gap: -0.0579
- Runtime seconds: 20.039639

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Fine-grained exploration.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_raw_gini_not_materially_worse

Log truncated: False
