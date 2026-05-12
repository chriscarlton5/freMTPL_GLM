# lightgbm_191_mid

## Hypothesis
Slightly higher randomization.

## Candidate Change
0.191 mid: feature 0.52 / bagging 0.52 + 16/24. Slightly higher than 0.515.

## CV Metric Summary
- Capped pure premium Gini: 0.1895
- Capped pure premium calibration gap: -0.0085
- Capped pure premium MAE: 218.234
- Raw pure premium Gini: 0.2126
- Raw pure premium calibration gap: -0.0654
- Runtime seconds: 25.101274

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
Fine-tune.

## Decision
keep

Gate failures: none

Log truncated: False
