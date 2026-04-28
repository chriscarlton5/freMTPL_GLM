# lightgbm_flexible_capped_severity

## Hypothesis
The segmentation champion may be limited by capped-severity ranking. A more flexible capped-severity component may improve capped pure premium Gini without weakening frequency or raw severity behavior.

## Candidate Change
Regularized LightGBM challenger that keeps the current frequency and raw severity grids but gives capped severity a more flexible grid.

## CV Metric Summary
- Capped pure premium Gini: 0.1839
- Capped pure premium calibration gap: -0.0172
- Capped pure premium MAE: 217.3112
- Raw pure premium Gini: 0.1976
- Raw pure premium calibration gap: -0.0469
- Runtime seconds: 21.850096

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| minimum_capped_gini_gain | False |
| minimum_fold_agreement | True |
| capped_calibration_tolerance | True |
| capped_mae_tolerance | True |
| capped_rmse_tolerance | True |
| raw_gini_not_materially_worse | True |

## Actuarial Interpretation
Capped severity is the stability-oriented severity view. Flexibility is increased only there, while the frequency and raw severity components remain on the current constrained grids.

## Decision
discard

Gate failures: minimum_capped_gini_gain

Log truncated: False
