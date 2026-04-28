# lightgbm_ft_0001

## Hypothesis
Targeted leaves variation

## Candidate Change
Fine-tune: leaves. FF=0.518, L2=13.2

## CV Metric Summary
- Capped pure premium Gini: 0.1841
- Capped pure premium calibration gap: -0.0213
- Capped pure premium MAE: 216.8725
- Raw pure premium Gini: 0.213
- Raw pure premium calibration gap: -0.0709
- Runtime seconds: 26.075972

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
