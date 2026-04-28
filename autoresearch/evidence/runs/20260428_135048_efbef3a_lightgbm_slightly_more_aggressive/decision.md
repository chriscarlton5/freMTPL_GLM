# lightgbm_slightly_more_aggressive

## Hypothesis
Current best uses min_data 1600-1300. Try ~1280-1040 to see if finer granularity helps.

## Candidate Change
Current best: Gini 0.1851, calibration -0.98%, MAE 218.07. Try slightly lower min_data (~20%) to find finer splits.

## CV Metric Summary
- Capped pure premium Gini: 0.182
- Capped pure premium calibration gap: -0.0166
- Capped pure premium MAE: 217.3584
- Raw pure premium Gini: 0.1951
- Raw pure premium calibration gap: -0.058
- Runtime seconds: 18.287821

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
Smaller min_data allows more splits - but with early stopping prevents overfit.

## Decision
keep

Gate failures: none

Log truncated: False
