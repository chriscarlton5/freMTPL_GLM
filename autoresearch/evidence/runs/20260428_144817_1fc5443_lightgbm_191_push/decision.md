# lightgbm_191_push

## Hypothesis
Push 0.19+ barrier.

## Candidate Change
0.191 push: feature 0.512 / bagging 0.512 + 16/24 + L2 12.8/10.8. Push beyond 0.1908.

## CV Metric Summary
- Capped pure premium Gini: 0.1848
- Capped pure premium calibration gap: -0.0198
- Capped pure premium MAE: 217.0442
- Raw pure premium Gini: 0.213
- Raw pure premium calibration gap: -0.0659
- Runtime seconds: 25.581148

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
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Maximum push.

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
