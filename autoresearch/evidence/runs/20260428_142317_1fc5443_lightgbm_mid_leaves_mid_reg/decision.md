# lightgbm_mid_leaves_mid_reg

## Hypothesis
Mid-range exploration.

## Candidate Change
NEW: Mid leaves (16/22) mid L2 (7) - search middle ground. Previous best 0.1851-0.1852.

## CV Metric Summary
- Capped pure premium Gini: 0.1831
- Capped pure premium calibration gap: -0.017
- Capped pure premium MAE: 217.3157
- Raw pure premium Gini: 0.1942
- Raw pure premium calibration gap: -0.0501
- Runtime seconds: 18.297544

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
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Search middle.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
