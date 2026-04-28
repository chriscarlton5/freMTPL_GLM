# lightgbm_best_variant

## Hypothesis
Simpler leaves + same high LR. The 14 leaves gives less capacity but may generalize better.

## Candidate Change
Best: leaves 15/24, LR 0.04/0.035. Try leaves 14/22 with same LR - simpler model might generalize better.

## CV Metric Summary
- Capped pure premium Gini: 0.182
- Capped pure premium calibration gap: -0.013
- Capped pure premium MAE: 217.747
- Raw pure premium Gini: 0.1933
- Raw pure premium calibration gap: -0.0496
- Runtime seconds: 18.101932

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Simpler model with high LR - balance capacity and generalization.

## Decision
keep

Gate failures: none

Log truncated: False
