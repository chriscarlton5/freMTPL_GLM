# enhanced_glm_power_brand_frequency_capped

## Hypothesis
Power:Brand frequency improved raw ranking while Power:Brand capped severity slightly improved capped MAE and calibration. Combining the two transparent terms may produce enough stable pure premium movement to clear the pricing gate.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to frequency and capped severity.

## CV Metric Summary
- Capped pure premium Gini: 0.1673
- Capped pure premium calibration gap: 0.001
- Capped pure premium MAE: 218.9907
- Raw pure premium Gini: 0.1565
- Raw pure premium calibration gap: 0.003
- Runtime seconds: 105.786256

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
Vehicle power and brand are standard actuarial rating dimensions. The combined term set is still transparent, but it adds many sparse cells, so it must improve ranking or error enough to justify its complexity.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
