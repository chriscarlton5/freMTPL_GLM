# lightgbm_best_plus_min_data

## Hypothesis
The best run (0.1845) used min_data 1600-2000. Try reducing to 1200-1500 for more granularity while keeping strong L2.

## Candidate Change
LightGBM with best LR (0.038) but slightly lower min_data_in_leaf to allow more granular splits. Keep regularization.

## CV Metric Summary
- Capped pure premium Gini: 0.183
- Capped pure premium calibration gap: -0.0129
- Capped pure premium MAE: 217.775
- Raw pure premium Gini: 0.2009
- Raw pure premium calibration gap: -0.05
- Runtime seconds: 18.90963

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
Lower min_data allows more splits - but with early stopping and L2. Actuaries balance complexity vs stability.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
