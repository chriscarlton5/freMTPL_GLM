# enhanced_glm_driver_car_age_capped_severity

## Hypothesis
The GBM interaction review showed large age-by-vehicle-age pure premium differences. Putting this term in capped severity may improve stable loss-cost ranking while leaving frequency calibration intact.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds DriverAgeBand:CarAgeBand to the capped severity component only.

## CV Metric Summary
- Capped pure premium Gini: 0.1581
- Capped pure premium calibration gap: 0.0029
- Capped pure premium MAE: 219.2095
- Raw pure premium Gini: 0.154
- Raw pure premium calibration gap: 0.0028
- Runtime seconds: 22.591607

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Driver age and vehicle age have plausible claim-size relationships, but severity is tail-sensitive. This candidate uses the capped target only and requires cross-fold support before any pricing-level change.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
