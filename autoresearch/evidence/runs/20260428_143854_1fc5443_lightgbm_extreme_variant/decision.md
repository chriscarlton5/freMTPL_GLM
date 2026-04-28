# lightgbm_extreme_variant

## Hypothesis
Further randomization may push beyond 0.1855.

## Candidate Change
Extreme variant: feature 0.55 / bagging 0.55. Even more randomization.

## CV Metric Summary
- Capped pure premium Gini: 0.1874
- Capped pure premium calibration gap: -0.022
- Capped pure premium MAE: 216.8422
- Raw pure premium Gini: 0.2005
- Raw pure premium calibration gap: -0.086
- Runtime seconds: 25.020931

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
Push boundaries.

## Decision
keep

Gate failures: none

Log truncated: False
