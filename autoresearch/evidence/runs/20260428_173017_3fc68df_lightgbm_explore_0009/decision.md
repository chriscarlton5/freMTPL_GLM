# lightgbm_explore_0009

## Hypothesis
EXPLORE approach

## Candidate Change
EXPLORE: FF=0.499 L2=10.2 L=17

## CV Metric Summary
- Capped pure premium Gini: 0.1849
- Capped pure premium calibration gap: -0.0187
- Capped pure premium MAE: 217.2567
- Raw pure premium Gini: 0.2123
- Raw pure premium calibration gap: -0.0741
- Runtime seconds: 32.161306

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
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Autonomous research

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
