# lightgbm_191_exact

## Hypothesis
Exact match of record config.

## Candidate Change
0.191 exact: feature 0.515 / bagging 0.515 + 16/24 + exact L2 from 0.1908. Exact reproduction attempt.

## CV Metric Summary
- Capped pure premium Gini: 0.1908
- Capped pure premium calibration gap: -0.0097
- Capped pure premium MAE: 218.1051
- Raw pure premium Gini: 0.2137
- Raw pure premium calibration gap: -0.0659
- Runtime seconds: 25.395932

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
Verify exact config.

## Decision
keep

Gate failures: none

Log truncated: False
