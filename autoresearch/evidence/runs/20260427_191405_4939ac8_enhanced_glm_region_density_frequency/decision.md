# enhanced_glm_region_density_frequency

## Hypothesis
Regional density interaction may recover transparent frequency segmentation that the LightGBM found, while preserving the pricing GLM's strong capped pure premium calibration.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Region:DensityBand to the frequency component only.

## CV Metric Summary
- Capped pure premium Gini: 0.1658
- Capped pure premium calibration gap: 0.0019
- Capped pure premium MAE: 219.0672
- Raw pure premium Gini: 0.1513
- Raw pure premium calibration gap: 0.0029
- Runtime seconds: 35.825063

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Territory and density are plausible exposure/risk modifiers, but the term is kept in frequency only because claim count is the more stable component for geographic segmentation. The interaction remains auditable as a banded GLM term.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
