# lightgbm_deeper_boosting

## Hypothesis
The tuned aggressive LGBM hit 0.1841 Gini (+0.0014 vs champion). Need +0.005. More boosting rounds and deeper trees should help. Strong L2 still prevents overfitting.

## Candidate Change
LightGBM with more boosting rounds (150+), deeper trees to capture complex patterns. Keep strong regularization to prevent overfit. Goal: clear 0.005 Gini threshold vs champion.

## CV Metric Summary
- Capped pure premium Gini: 0.1817
- Capped pure premium calibration gap: -0.0121
- Capped pure premium MAE: 217.8317
- Raw pure premium Gini: 0.1935
- Raw pure premium calibration gap: -0.0617
- Runtime seconds: 22.750642

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
More boosting rounds with early stopping is standard - model stops when validation stops improving. Strong regularization (L2=10) keeps it defensible. Full documentation of hyperparameters and validation.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
