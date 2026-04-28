# lightgbm_optimal_balance_v2

## Hypothesis
Combine optimal LR with optimal leaves. May get best of both.

## Candidate Change
Combine findings: aggressive LR (0.05) with best settings (leaves 15/24). Best MAE was 216.90 with 0.1836 Gini. Try to get both.

## CV Metric Summary
- Capped pure premium Gini: 0.1823
- Capped pure premium calibration gap: -0.0199
- Capped pure premium MAE: 216.9821
- Raw pure premium Gini: 0.1956
- Raw pure premium calibration gap: -0.0491
- Runtime seconds: 17.91396

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
Synthesis of best hyperparameters.

## Decision
keep

Gate failures: none

Log truncated: False
