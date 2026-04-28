# simple_glm_power_brand_capped_severity

## Hypothesis
The Power:Brand capped-severity signal may not require spline flexibility. A simpler linear GLM could retain the small capped-pricing gain with better parsimony and stability.

## Candidate Change
Simpler GLM using linear DriverAge, CarAge, and logDensity terms in all components; adds Power:Brand to capped severity only.

## CV Metric Summary
- Capped pure premium Gini: 0.1366
- Capped pure premium calibration gap: -0.0006
- Capped pure premium MAE: 219.3652
- Raw pure premium Gini: 0.1423
- Raw pure premium calibration gap: 0.0088
- Runtime seconds: 17.873216

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is a transparent parsimony test. Linear continuous effects are easier to explain than splines, but the model must not give up too much predictive power or calibration.

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
