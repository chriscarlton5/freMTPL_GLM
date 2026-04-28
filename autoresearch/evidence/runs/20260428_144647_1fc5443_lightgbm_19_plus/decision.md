# lightgbm_19_plus

## Hypothesis
Pushing beyond 0.19.

## Candidate Change
19+ push: feature 0.508 / bagging 0.508 + 15/23 + lower min_data. Push above 0.19.

## CV Metric Summary
- Capped pure premium Gini: 0.1833
- Capped pure premium calibration gap: -0.0187
- Capped pure premium MAE: 217.1576
- Raw pure premium Gini: 0.21
- Raw pure premium calibration gap: -0.0732
- Runtime seconds: 25.062806

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
| segmentation_raw_gini_not_materially_worse | True |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Push further.

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
