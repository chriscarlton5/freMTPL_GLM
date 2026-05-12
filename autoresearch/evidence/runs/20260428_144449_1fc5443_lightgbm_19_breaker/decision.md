# lightgbm_19_breaker

## Hypothesis
Breaking 0.19 barrier.

## Candidate Change
0.19 breaker: feature 0.51 / bagging 0.51 + 15/23 leaves + slightly lower L2. Push for 0.19+.

## CV Metric Summary
- Capped pure premium Gini: 0.1842
- Capped pure premium calibration gap: -0.021
- Capped pure premium MAE: 216.9296
- Raw pure premium Gini: 0.2103
- Raw pure premium calibration gap: -0.0725
- Runtime seconds: 24.796598

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
Push boundaries.

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
