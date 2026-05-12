# lightgbm_fewer_leaves_better

## Hypothesis
Simpler model might outperform complex. Less overfitting risk. Classic bias-variance tradeoff.

## Candidate Change
NEW HYPOTHESIS: Try simpler model - fewer leaves (12/20 vs 15/24). May generalize better despite less capacity.

## CV Metric Summary
- Capped pure premium Gini: 0.1829
- Capped pure premium calibration gap: -0.0115
- Capped pure premium MAE: 217.8869
- Raw pure premium Gini: 0.1991
- Raw pure premium calibration gap: -0.0519
- Runtime seconds: 17.193972

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
Parsimony principle: simpler model preferred when similar performance.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
