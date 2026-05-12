# lightgbm_ft_0003

## Hypothesis
Targeted min_data variation

## Candidate Change
Fine-tune: min_data. FF=0.518, L2=13.2

## CV Metric Summary
- Capped pure premium Gini: 0.1844
- Capped pure premium calibration gap: -0.0215
- Capped pure premium MAE: 216.8578
- Raw pure premium Gini: 0.2128
- Raw pure premium calibration gap: -0.071
- Runtime seconds: 28.989671

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Exploiting sweet spot

## Decision
keep

Gate failures: none

Log truncated: False
