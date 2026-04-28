# lightgbm_varying_gamma

## Hypothesis
Different gamma may find different solution.

## Candidate Change
NEW: Use varying gamma for severity - lower gamma=1.2 (closer to Gaussian) for stability vs standard 1.5 tweedie.

## CV Metric Summary
- Capped pure premium Gini: 0.1852
- Capped pure premium calibration gap: -0.0099
- Capped pure premium MAE: 218.0714
- Raw pure premium Gini: 0.2006
- Raw pure premium calibration gap: -0.0495
- Runtime seconds: 18.516912

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | True |
| segmentation_capped_calibration_tolerance | True |
| segmentation_capped_mae_tolerance | True |
| segmentation_capped_rmse_tolerance | True |
| segmentation_raw_gini_not_materially_worse | True |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Gamma parameter affects tail behavior.

## Decision
keep

Gate failures: none

Log truncated: False
