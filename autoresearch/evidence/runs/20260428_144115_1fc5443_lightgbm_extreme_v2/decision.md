# lightgbm_extreme_v2

## Hypothesis
Variation may push further.

## Candidate Change
Extreme v2: feature 0.54 / bagging 0.54 + 17/26 leaves + lower L2. Variation on 0.1874 winner.

## CV Metric Summary
- Capped pure premium Gini: 0.1864
- Capped pure premium calibration gap: -0.0159
- Capped pure premium MAE: 217.4789
- Raw pure premium Gini: 0.2105
- Raw pure premium calibration gap: -0.0726
- Runtime seconds: 24.983089

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
Fine variation.

## Decision
keep

Gate failures: none

Log truncated: False
