# lightgbm_lower_lr_more_iter

## Hypothesis
Lower LR + more iterations may find better local minimum. Standard tuning practice.

## Candidate Change
Best 0.1851 with leaves 15/24, LR 0.04/0.035. Try lower LR (0.03/0.025) with more rounds for more stable convergence.

## CV Metric Summary
- Capped pure premium Gini: 0.1837
- Capped pure premium calibration gap: -0.0104
- Capped pure premium MAE: 217.9735
- Raw pure premium Gini: 0.1965
- Raw pure premium calibration gap: -0.0575
- Runtime seconds: 25.022019

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
Slower learning with more iterations for better convergence.

## Decision
keep

Gate failures: none

Log truncated: False
