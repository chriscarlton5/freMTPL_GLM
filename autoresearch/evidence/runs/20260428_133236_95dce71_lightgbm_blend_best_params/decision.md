# lightgbm_blend_best_params

## Hypothesis
Combine the best hyperparameters found: higher LR from best run + balanced tree depth. Target 0.185+ Gini.

## Candidate Change
Blend of best params: tuned aggressive num_leaves (12-20), high LR from best run (0.038), moderate bagging (0.88). Combination that hit 0.1845 Gini as base.

## CV Metric Summary
- Capped pure premium Gini: 0.18
- Capped pure premium calibration gap: -0.0126
- Capped pure premium MAE: 217.8363
- Raw pure premium Gini: 0.1863
- Raw pure premium calibration gap: -0.0557
- Runtime seconds: 17.978969

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Standard hyperparameter tuning - combine best settings found. Still regularized to maintain defensibility.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
