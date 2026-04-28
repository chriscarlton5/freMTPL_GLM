# lightgbm_midleaf_frequency_probe

## Hypothesis
The current segmentation champion is weakest on fold 2 capped pure premium Gini. A moderately less-smoothed frequency option may improve frequency ranking in that fold while retaining enough regularization to avoid broad calibration deterioration.

## Candidate Change
LightGBM challenger that keeps champion severity and capped severity settings while adding one mid-leaf frequency option from the original GBM analysis grid.

## CV Metric Summary
- Capped pure premium Gini: 0.1847
- Capped pure premium calibration gap: -0.0144
- Capped pure premium MAE: 217.5436
- Raw pure premium Gini: 0.1953
- Raw pure premium calibration gap: -0.0474
- Runtime seconds: 23.586487

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
This remains segmentation research only. Frequency is a stable and actuarially interpretable source of MTPL segmentation, and severity is held fixed so any movement is attributable to claim-count ranking.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
