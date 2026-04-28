# glm_baseline_plus_spline_degrees

## Hypothesis
The LightGBM advantage appears structural. Try max GLM flexibility via higher spline df to get as close as possible. This tests whether GLM can get within 1% of LightGBM on ranking.

## Candidate Change
GLM baseline with increased spline degrees (df=6 vs df=5). Conservative enhancement - higher flexibility in continuous terms only, no interactions that could cause instability.

## CV Metric Summary
- Capped pure premium Gini: 0.1684
- Capped pure premium calibration gap: 0.0019
- Capped pure premium MAE: 219.0904
- Raw pure premium Gini: 0.154
- Raw pure premium calibration gap: 0.0028
- Runtime seconds: 21.477502

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
GLM with higher df splines is fully transparent. Actuaries often use degree 4-6 splines. This is within standard practice and auditable. No interactions = no sparse cell risk.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
