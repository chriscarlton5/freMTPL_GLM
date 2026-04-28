# lightgbm_diverse_v2

## Hypothesis
More randomization may push beyond 0.1897.

## Candidate Change
Diverse v2: feature 0.50 / bagging 0.50 + 14/22 leaves. Push randomization further.

## CV Metric Summary
- Capped pure premium Gini: 0.1857
- Capped pure premium calibration gap: -0.0256
- Capped pure premium MAE: 216.4198
- Raw pure premium Gini: 0.2042
- Raw pure premium calibration gap: -0.0651
- Runtime seconds: 27.138966

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Push boundaries.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
