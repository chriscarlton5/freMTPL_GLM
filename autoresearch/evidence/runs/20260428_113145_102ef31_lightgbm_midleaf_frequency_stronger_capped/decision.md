# lightgbm_midleaf_frequency_stronger_capped

## Hypothesis
The forced aggressive capped candidate passed fold agreement and reached capped Gini 0.1864. Slightly stronger capped-severity flexibility may add the remaining lift needed to clear the 0.005 champion gain gate without breaking calibration.

## Candidate Change
LightGBM challenger combining the mid-leaf frequency probe with a stronger forced capped-severity grid to test whether the recent near-miss can clear the segmentation Gini threshold.

## CV Metric Summary
- Capped pure premium Gini: 0.1875
- Capped pure premium calibration gap: -0.0152
- Capped pure premium MAE: 217.4857
- Raw pure premium Gini: 0.1953
- Raw pure premium calibration gap: -0.0474
- Runtime seconds: 23.913611

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
This is a high-risk segmentation-only experiment. It is acceptable only if the lift remains broad across folds; otherwise it is evidence that capped severity flexibility is no longer actuarially defensible.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
