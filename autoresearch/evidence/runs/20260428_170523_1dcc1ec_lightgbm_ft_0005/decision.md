# lightgbm_ft_0005

## Hypothesis
Targeted combo variation

## Candidate Change
Fine-tune: combo. FF=0.510, L2=13.7

## CV Metric Summary
- Capped pure premium Gini: 0.186
- Capped pure premium calibration gap: -0.0222
- Capped pure premium MAE: 216.7797
- Raw pure premium Gini: 0.2153
- Raw pure premium calibration gap: -0.0647
- Runtime seconds: 28.709782

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
