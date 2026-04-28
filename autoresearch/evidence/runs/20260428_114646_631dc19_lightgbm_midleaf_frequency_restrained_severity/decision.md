# lightgbm_midleaf_frequency_restrained_severity

## Hypothesis
The strongest near misses came from mid-leaf frequency lift plus capped-severity flexibility. Holding severity conservative may retain the frequency ranking signal while avoiding capped severity overfit.

## Candidate Change
LightGBM challenger adding one mid-leaf frequency option while restraining raw and capped severity grids to conservative leaf sizes.

## CV Metric Summary
- Capped pure premium Gini: 0.1818
- Capped pure premium calibration gap: -0.0141
- Capped pure premium MAE: 217.5967
- Raw pure premium Gini: 0.1902
- Raw pure premium calibration gap: -0.0395
- Runtime seconds: 18.521573

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is a segmentation research candidate, not a pricing-level model. It tests whether the incremental lift is coming from a plausible claim frequency segmentation signal rather than unstable severity slicing.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
