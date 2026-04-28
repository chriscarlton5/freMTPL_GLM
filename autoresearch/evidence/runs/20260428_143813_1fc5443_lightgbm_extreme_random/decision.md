# lightgbm_extreme_random

## Hypothesis
Even more randomization may help.

## Candidate Change
Extreme randomization: feature 0.6 / bagging 0.6. Maximum diversity from standard config.

## CV Metric Summary
- Capped pure premium Gini: 0.1855
- Capped pure premium calibration gap: -0.0207
- Capped pure premium MAE: 216.9655
- Raw pure premium Gini: 0.2025
- Raw pure premium calibration gap: -0.0429
- Runtime seconds: 22.88989

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
Extreme exploration.

## Decision
keep

Gate failures: none

Log truncated: False
