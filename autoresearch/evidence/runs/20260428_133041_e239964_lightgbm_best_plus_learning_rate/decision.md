# lightgbm_best_plus_learning_rate

## Hypothesis
Tuned aggressive achieved 0.1841 Gini but narrowly missed 0.005 threshold. Try slightly higher learning rate to find better local minimum.

## Candidate Change
Based on best run (tuned aggressive 0.1841 Gini) with slight learning rate adjustment. Higher learning rate may find better optima.

## CV Metric Summary
- Capped pure premium Gini: 0.1845
- Capped pure premium calibration gap: -0.0127
- Capped pure premium MAE: 217.8044
- Raw pure premium Gini: 0.202
- Raw pure premium calibration gap: -0.0381
- Runtime seconds: 17.852909

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
Standard practice to tune learning rate. With early stopping, higher rate is safe. Full documentation maintained.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
