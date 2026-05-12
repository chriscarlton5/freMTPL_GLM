# lightgbm_higher_early_stop

## Hypothesis
Current uses 15 rounds. Higher allows model more iterations to find optimal. May prevent early underfitting.

## Candidate Change
NEW HYPOTHESIS: Use more aggressive early stopping (25-30 rounds vs 15). Find more optimal stopping point - less overfitting.

## CV Metric Summary
- Capped pure premium Gini: 0.1844
- Capped pure premium calibration gap: -0.0098
- Capped pure premium MAE: 218.0196
- Raw pure premium Gini: 0.1999
- Raw pure premium calibration gap: -0.0493
- Runtime seconds: 19.497034

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
Early stopping is critical hyperparameter. Standard practice to tune.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
