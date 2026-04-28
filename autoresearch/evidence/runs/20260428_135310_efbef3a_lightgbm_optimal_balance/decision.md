# lightgbm_optimal_balance

## Hypothesis
15/24 @ 0.04 = 0.1851, 16/28 @ 0.04 = 0.1834. Try 16/23 with 0.042 LR.

## Candidate Change
Best still 0.1851. Try intermediate: 16/23 leaves, 0.042 LR to find optimum between capacity and overfitting.

## CV Metric Summary
- Capped pure premium Gini: 0.1848
- Capped pure premium calibration gap: -0.0119
- Capped pure premium MAE: 217.8111
- Raw pure premium Gini: 0.1934
- Raw pure premium calibration gap: -0.0543
- Runtime seconds: 19.305277

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
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Balance between best configs - fine-tuned hyperparameter search.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain

Log truncated: False
