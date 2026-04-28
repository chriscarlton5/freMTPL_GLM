# lightgbm_ps_0001

## Hypothesis
ps

## Candidate Change
ps: FF=0.480 L2=12.5

## CV Metric Summary
- Capped pure premium Gini: 0.1835
- Capped pure premium calibration gap: -0.0199
- Capped pure premium MAE: 217.0585
- Raw pure premium Gini: 0.2121
- Raw pure premium calibration gap: -0.0781
- Runtime seconds: 28.738412

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
auto

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
