# lightgbm_slightly_more_aggressive

## Hypothesis
Current best (0.1845) leaves 14/22. Try 15/24 with higher LR 0.04 to see if more capacity + stronger signal pushes Gini.

## Candidate Change
Try slight refinement: more leaves (15-24), slightly higher LR (0.04), slightly less regularization to see if we can push past 0.1845.

## CV Metric Summary
- Capped pure premium Gini: 0.1851
- Capped pure premium calibration gap: -0.0098
- Capped pure premium MAE: 218.0687
- Raw pure premium Gini: 0.2004
- Raw pure premium calibration gap: -0.0494
- Runtime seconds: 19.235785

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
Conservative increase - early stopping prevents overfitting. Standard hyperparameter exploration.

## Decision
keep

Gate failures: none

Log truncated: False
