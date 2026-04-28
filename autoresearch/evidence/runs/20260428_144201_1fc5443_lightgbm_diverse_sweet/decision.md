# lightgbm_diverse_sweet

## Hypothesis
Different leaf combination may work.

## Candidate Change
Diverse sweet: feature 0.52 / bagging 0.52 + 15/23 leaves + moderate L2. Different leaf config.

## CV Metric Summary
- Capped pure premium Gini: 0.1897
- Capped pure premium calibration gap: -0.0115
- Capped pure premium MAE: 217.928
- Raw pure premium Gini: 0.214
- Raw pure premium calibration gap: -0.0645
- Runtime seconds: 24.924211

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | True |
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
Leaf variation.

## Decision
keep

Gate failures: none

Log truncated: False
