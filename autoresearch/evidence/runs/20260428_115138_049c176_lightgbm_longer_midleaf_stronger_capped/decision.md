# lightgbm_longer_midleaf_stronger_capped

## Hypothesis
The strongest near miss missed the segmentation Gini gate by 0.0002. Keeping its shape but allowing more early-stopped boosting rounds may recover a small amount of ranking lift without adding new flexibility.

## Candidate Change
LightGBM challenger using the strongest mid-leaf frequency plus stronger capped-severity near-miss grids with a longer early-stopped boosting budget.

## CV Metric Summary
- Capped pure premium Gini: 0.1828
- Capped pure premium calibration gap: -0.0261
- Capped pure premium MAE: 216.3352
- Raw pure premium Gini: 0.1964
- Raw pure premium calibration gap: -0.0467
- Runtime seconds: 31.051123

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is a segmentation-only sensitivity test around the best near miss. It should be rejected unless the lift clears the predefined gate and remains broad across folds.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
