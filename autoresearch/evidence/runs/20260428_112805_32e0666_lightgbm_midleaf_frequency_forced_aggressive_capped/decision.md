# lightgbm_midleaf_frequency_forced_aggressive_capped

## Hypothesis
Mid-leaf frequency improved capped Gini with fold agreement, while the aggressive capped-severity run produced the highest mean capped Gini so far. Combining them may clear the segmentation Gini threshold, though it must still pass fold agreement and calibration gates.

## Candidate Change
LightGBM challenger combining the mid-leaf frequency probe with a forced aggressive capped-severity grid, while keeping raw severity at the champion settings.

## CV Metric Summary
- Capped pure premium Gini: 0.1864
- Capped pure premium calibration gap: -0.0095
- Capped pure premium MAE: 218.1193
- Raw pure premium Gini: 0.1953
- Raw pure premium calibration gap: -0.0474
- Runtime seconds: 23.095956

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is an intentionally aggressive segmentation-research test, not a pricing-level candidate. It is only acceptable if the ranking lift is broad across folds and the capped severity flexibility does not create unexplained instability.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
