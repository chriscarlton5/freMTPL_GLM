# lightgbm_ft_0030

## Hypothesis
ft

## Candidate Change
ft: FF=0.508 L2=13.3

## CV Metric Summary
- Capped pure premium Gini: 0.1848
- Capped pure premium calibration gap: -0.0219
- Capped pure premium MAE: 216.8248
- Raw pure premium Gini: 0.2128
- Raw pure premium calibration gap: -0.0667
- Runtime seconds: 29.017886

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
auto

## Decision
discard

Gate failures: pricing_material_improvement, pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
