# lightgbm_midleaf_frequency_mild_capped

## Hypothesis
The mid-leaf frequency option passed fold agreement but missed the minimum Gini gain. Adding a mild capped-severity option may provide enough additional capped pure premium lift while preserving the fold agreement and MAE improvements.

## Candidate Change
LightGBM challenger combining the mid-leaf frequency probe with one mild capped-severity option while retaining all champion grid options.

## CV Metric Summary
- Capped pure premium Gini: 0.1847
- Capped pure premium calibration gap: -0.0144
- Capped pure premium MAE: 217.5436
- Raw pure premium Gini: 0.1953
- Raw pure premium calibration gap: -0.0474
- Runtime seconds: 24.428828

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
This combines two near-miss ideas sparingly. Frequency remains the primary stable signal, while capped severity gets only one additional regularized option rather than another broad severity search.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
