# lightgbm_ft_0006

## Hypothesis
Targeted l2 variation

## Candidate Change
Fine-tune: l2. FF=0.515, L2=13.3

## CV Metric Summary
- Capped pure premium Gini: 0.1905
- Capped pure premium calibration gap: -0.0072
- Capped pure premium MAE: 218.3598
- Raw pure premium Gini: 0.2064
- Raw pure premium calibration gap: -0.0679
- Runtime seconds: 27.747148

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Exploiting sweet spot

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_raw_gini_not_materially_worse

Log truncated: False
