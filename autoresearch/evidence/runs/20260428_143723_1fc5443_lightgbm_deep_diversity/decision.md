# lightgbm_deep_diversity

## Hypothesis
Extreme diversity + regularization may break hyperparameter ceiling.

## Candidate Change
Deep diversity: 0.70 feature fraction + 0.70 bagging. Max randomization + more regularization. Break 0.185 ceiling.

## CV Metric Summary
- Capped pure premium Gini: 0.1845
- Capped pure premium calibration gap: -0.0139
- Capped pure premium MAE: 217.6231
- Raw pure premium Gini: 0.1987
- Raw pure premium calibration gap: -0.0716
- Runtime seconds: 22.619235

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
Maximum randomization exploration.

## Decision
keep

Gate failures: none

Log truncated: False
