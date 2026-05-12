# lightgbm_midleaf_frequency_edge_capped

## Hypothesis
The previous stronger capped candidate missed the segmentation Gini gate by 0.0002 with all folds improved. A small adjacent capped severity adjustment may clear the gate while remaining inside the calibration and error tolerances.

## Candidate Change
LightGBM challenger using the mid-leaf frequency probe with one edge capped-severity grid adjacent to the strongest near miss.

## CV Metric Summary
- Capped pure premium Gini: 0.1845
- Capped pure premium calibration gap: -0.0345
- Capped pure premium MAE: 215.4923
- Raw pure premium Gini: 0.1953
- Raw pure premium calibration gap: -0.0474
- Runtime seconds: 23.153069

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
This is the last justified local search around the capped-severity edge. It is segmentation research only and must be rejected if the incremental lift is not broad and stable.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
