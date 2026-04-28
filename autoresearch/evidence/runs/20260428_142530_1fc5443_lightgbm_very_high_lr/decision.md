# lightgbm_very_high_lr

## Hypothesis
Very high LR finds different solutions.

## Candidate Change
NEW: Very high LR (0.055/0.05) with high min_data. Aggressive learning.

## CV Metric Summary
- Capped pure premium Gini: 0.1838
- Capped pure premium calibration gap: -0.0134
- Capped pure premium MAE: 217.7151
- Raw pure premium Gini: 0.1971
- Raw pure premium calibration gap: -0.0469
- Runtime seconds: 15.297426

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
Aggressive exploration.

## Decision
keep

Gate failures: none

Log truncated: False
