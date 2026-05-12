# lightgbm_diverse_v3

## Hypothesis
Fine-tune the sweet spot.

## Candidate Change
Diverse v3: feature 0.53 / bagging 0.53 + 16/24 leaves. Fine-tune around 0.1897 winner.

## CV Metric Summary
- Capped pure premium Gini: 0.1849
- Capped pure premium calibration gap: -0.0136
- Capped pure premium MAE: 217.7332
- Raw pure premium Gini: 0.2123
- Raw pure premium calibration gap: -0.0748
- Runtime seconds: 25.028488

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
Refine sweet spot.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
