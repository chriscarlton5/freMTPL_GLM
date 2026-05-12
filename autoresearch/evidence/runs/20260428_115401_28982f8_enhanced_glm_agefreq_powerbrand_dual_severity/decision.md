# enhanced_glm_agefreq_powerbrand_dual_severity

## Hypothesis
The strongest transparent frequency and severity near misses may be complementary: age-car segmentation captures claim propensity while Power:Brand captures repair-cost severity.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in all components; adds DriverAgeBand:CarAgeBand to frequency and Power:Brand to raw and capped severity.

## CV Metric Summary
- Capped pure premium Gini: 0.1678
- Capped pure premium calibration gap: -0.0011
- Capped pure premium MAE: 218.7821
- Raw pure premium Gini: 0.1643
- Raw pure premium calibration gap: -0.0015
- Runtime seconds: 43.657381

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
Driver age, car age, power, and brand are plausible rating dimensions. The combined interaction set remains interpretable but must overcome a high parsimony burden and sparse-cell stability risk.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
