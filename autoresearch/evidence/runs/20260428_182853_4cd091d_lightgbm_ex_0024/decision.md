# lightgbm_ex_0024

## Hypothesis
ex

## Candidate Change
ex: FF=0.534 L2=10.6

## CV Metric Summary
- Capped pure premium Gini: 0.1861
- Capped pure premium calibration gap: -0.0197
- Capped pure premium MAE: 217.0753
- Raw pure premium Gini: 0.2099
- Raw pure premium calibration gap: -0.0859
- Runtime seconds: 29.649102

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
auto

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
