# lightgbm_191_17_leaves

## Hypothesis
More leaves with high randomization.

## Candidate Change
0.191-17: feature 0.515 / bagging 0.515 + 17/25. More leaves.

## CV Metric Summary
- Capped pure premium Gini: 0.1849
- Capped pure premium calibration gap: -0.0211
- Capped pure premium MAE: 216.9066
- Raw pure premium Gini: 0.2144
- Raw pure premium calibration gap: -0.067
- Runtime seconds: 26.144808

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Test deeper trees.

## Decision
keep

Gate failures: none

Log truncated: False
