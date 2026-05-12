# enhanced_glm_power_brand_raw_severity

## Hypothesis
Power:Brand materially improved raw monitoring when added to both severity components. Restricting it to raw severity may keep that signal while avoiding extra capped-pricing complexity.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to raw severity only.

## CV Metric Summary
- Capped pure premium Gini: 0.1684
- Capped pure premium calibration gap: 0.0019
- Capped pure premium MAE: 219.0904
- Raw pure premium Gini: 0.1624
- Raw pure premium calibration gap: -0.0015
- Runtime seconds: 25.386625

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
Power and brand are plausible repair-cost variables for large raw claims. This candidate intentionally leaves capped severity unchanged to protect the stable pricing target.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
