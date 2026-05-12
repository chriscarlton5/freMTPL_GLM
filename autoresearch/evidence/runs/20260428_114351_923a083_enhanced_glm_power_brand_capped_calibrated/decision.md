# enhanced_glm_power_brand_capped_calibrated

## Hypothesis
Power:Brand capped severity was the strongest transparent pricing near miss, improving capped Gini, calibration, and MAE slightly. Fold-internal calibration may turn that into a material pricing-level improvement without leakage.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to capped severity and applies component calibration scalars estimated inside each training fold.

## CV Metric Summary
- Capped pure premium Gini: 0.1675
- Capped pure premium calibration gap: 0.0265
- Capped pure premium MAE: 221.5002
- Raw pure premium Gini: 0.1467
- Raw pure premium calibration gap: 0.1071
- Runtime seconds: 23.492347

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | False |
| segmentation_capped_calibration_tolerance | True |
| segmentation_capped_mae_tolerance | False |
| segmentation_capped_rmse_tolerance | True |
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | False |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is a transparent pricing candidate. Power and brand are plausible repair-cost dimensions, and calibration is estimated only inside each outer training fold to protect the validation fold.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, pricing_capped_calibration_tight, pricing_capped_mae_tolerance, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_capped_mae_tolerance, segmentation_raw_gini_not_materially_worse

Log truncated: False
