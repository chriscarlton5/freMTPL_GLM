# lightgbm_ultra_random

## Hypothesis
Ultra randomization may push even further.

## Candidate Change
Ultra randomization: feature 0.5 / bagging 0.5 + more leaves + higher L2. Maximum exploration.

## CV Metric Summary
- Capped pure premium Gini: 0.1843
- Capped pure premium calibration gap: -0.0225
- Capped pure premium MAE: 216.8161
- Raw pure premium Gini: 0.2054
- Raw pure premium calibration gap: -0.0732
- Runtime seconds: 28.703828

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
Maximum diversity exploration.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
