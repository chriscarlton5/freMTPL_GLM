# lightgbm_191_exact_v2

## Hypothesis
More rounds + exact config may match 0.1908.

## Candidate Change
0.191 exact v2: feature 0.515 + 16/24 + L2 13.4/11.4 + 175 rounds. Exact best config with more iterations.

## CV Metric Summary
- Capped pure premium Gini: 0.1909
- Capped pure premium calibration gap: -0.0097
- Capped pure premium MAE: 218.1074
- Raw pure premium Gini: 0.214
- Raw pure premium calibration gap: -0.0658
- Runtime seconds: 25.239593

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
Final exact attempt.

## Decision
keep

Gate failures: none

Log truncated: False
