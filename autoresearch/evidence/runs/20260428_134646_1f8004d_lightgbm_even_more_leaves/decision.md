# lightgbm_even_more_leaves

## Hypothesis
Previous run 0.1851 was better. Try more leaves for more capacity. May capture finer risk segments.

## Candidate Change
Best now at Gini 0.1851, -0.98% calibration. Try more leaves (16-28) to capture more complex patterns.

## CV Metric Summary
- Capped pure premium Gini: 0.1834
- Capped pure premium calibration gap: -0.0135
- Capped pure premium MAE: 217.6771
- Raw pure premium Gini: 0.1936
- Raw pure premium calibration gap: -0.0638
- Runtime seconds: 19.373077

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
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
More leaves = more capacity. Keep regularization high to prevent overfit.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
