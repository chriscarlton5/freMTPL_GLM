# lightgbm_ultra_regularized

## Hypothesis
The current segmentation champion (Gini 0.1827) loses on calibration (-1.45%). Stronger regularization should improve calibration while preserving the ranking signal that makes LightGBM better than GLM.

## Candidate Change
Ultra-regularized LightGBM with very conservative hyperparameters: fewer leaves (8-12), more data per leaf (2000+), stronger L2 (15+). Goal is better calibration while maintaining segmentation advantage.

## CV Metric Summary
- Capped pure premium Gini: 0.1788
- Capped pure premium calibration gap: -0.0095
- Capped pure premium MAE: 218.3261
- Raw pure premium Gini: 0.1949
- Raw pure premium calibration gap: -0.025
- Runtime seconds: 15.2652

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
LightGBM with strong regularization is defensible: the hyperparameters (num_leaves, min_data_in_leaf, lambda_l2) limit model complexity. Regularized boosting is standard practice in actuarial pricing. Cross-validation prevents overfitting. Full methodology documented.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
