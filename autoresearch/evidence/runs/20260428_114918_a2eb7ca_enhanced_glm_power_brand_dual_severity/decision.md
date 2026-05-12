# enhanced_glm_power_brand_dual_severity

## Hypothesis
Power:Brand in capped severity was the strongest transparent pricing near miss. Adding the same repair-cost interaction to raw severity may improve raw monitoring metrics while preserving the capped gain.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to both raw and capped severity.

## CV Metric Summary
- Capped pure premium Gini: 0.1688
- Capped pure premium calibration gap: -0.0011
- Capped pure premium MAE: 218.7901
- Raw pure premium Gini: 0.1624
- Raw pure premium calibration gap: -0.0015
- Runtime seconds: 29.859266

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
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Power and brand are plausible severity dimensions tied to vehicle repair cost. This remains a transparent GLM, but should be rejected if the extra sparse interaction complexity is not supported by CV metrics.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
