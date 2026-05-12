# lightgbm_best_191

## Hypothesis
High randomization approach

## Candidate Change
Best config: FF=0.515 L2=13.4 leaves=16/24

## CV Metric Summary
- Capped pure premium Gini: 0.1909
- Capped pure premium calibration gap: -0.0097
- Capped pure premium MAE: 218.1074
- Raw pure premium Gini: 0.214
- Raw pure premium calibration gap: -0.0658
- Runtime seconds: 25.725309

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Champion config

## Decision
keep

Gate failures: none

Log truncated: False
