# lightgbm_tuned_midleaf_stronger_capped

## Hypothesis
The stronger capped candidate missed the Gini gate by 0.0002. A small frequency learning-rate adjustment may add the remaining ranking lift while preserving the all-fold improvement pattern.

## Candidate Change
LightGBM challenger using a slightly more assertive mid-leaf frequency option with the stronger forced capped-severity grid that nearly cleared the segmentation gate.

## CV Metric Summary
- Capped pure premium Gini: 0.1859
- Capped pure premium calibration gap: -0.0154
- Capped pure premium MAE: 217.4513
- Raw pure premium Gini: 0.197
- Raw pure premium calibration gap: -0.0476
- Runtime seconds: 23.521888

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
This is a local sensitivity test around the best near miss. It remains segmentation research only and should be discarded unless the lift clears the predefined threshold without calibration or fold weakness.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
