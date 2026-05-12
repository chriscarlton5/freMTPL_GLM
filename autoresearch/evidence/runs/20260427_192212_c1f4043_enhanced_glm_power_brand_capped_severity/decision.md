# enhanced_glm_power_brand_capped_severity

## Hypothesis
Vehicle power and brand were material GBM severity features. A capped severity interaction may capture vehicle repair-cost segmentation while avoiding raw severity tail amplification.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to the capped severity component only.

## CV Metric Summary
- Capped pure premium Gini: 0.1688
- Capped pure premium calibration gap: -0.0011
- Capped pure premium MAE: 218.7901
- Raw pure premium Gini: 0.154
- Raw pure premium calibration gap: 0.0028
- Runtime seconds: 24.839179

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
Power and brand can plausibly affect repair costs, but this term has sparse cells. It is acceptable only if capped pure premium ranking, error, and fold agreement support the added complexity.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
