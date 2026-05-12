# lightgbm_ft_0003

## Hypothesis
Targeted leaves variation

## Candidate Change
Fine-tune: leaves. FF=0.512, L2=13.5

## CV Metric Summary
- Capped pure premium Gini: 0.1835
- Capped pure premium calibration gap: -0.02
- Capped pure premium MAE: 217.0302
- Raw pure premium Gini: 0.2109
- Raw pure premium calibration gap: -0.0713
- Runtime seconds: 27.87889

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
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Exploiting sweet spot

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
