# lightgbm_compact_search

## Hypothesis
Compact with more features.

## Candidate Change
NEW: Compact search 13-19 leaves, higher min_data, higher feature fraction. Different direction from standard.

## CV Metric Summary
- Capped pure premium Gini: 0.1816
- Capped pure premium calibration gap: -0.0118
- Capped pure premium MAE: 217.8841
- Raw pure premium Gini: 0.2016
- Raw pure premium calibration gap: -0.0399
- Runtime seconds: 17.816699

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
Compact model exploration.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
