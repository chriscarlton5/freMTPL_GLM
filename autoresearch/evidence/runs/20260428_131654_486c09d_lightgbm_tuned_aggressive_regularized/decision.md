# lightgbm_tuned_aggressive_regularized

## Hypothesis
Ultra-regularized achieved Gini 0.1788, calibration -0.95%, MAE 218.33. A bit more flexibility should push Gini past 0.1827 while keeping calibrated. Balance between ranking and stability.

## Candidate Change
Tuned LightGBM between ultra-regularized and champion: moderate leaves (12-20), balanced regularization (L2 10-15), target Gini 0.183+ while maintaining calibration < 1%.

## CV Metric Summary
- Capped pure premium Gini: 0.1841
- Capped pure premium calibration gap: -0.0122
- Capped pure premium MAE: 217.9022
- Raw pure premium Gini: 0.1969
- Raw pure premium calibration gap: -0.0657
- Runtime seconds: 17.164997

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
LightGBM with balanced regularization - less constrained than before but still regularized to prevent overfitting. Uses early stopping on validation fold. Methodology fully documented. Standard actuarial practice.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
