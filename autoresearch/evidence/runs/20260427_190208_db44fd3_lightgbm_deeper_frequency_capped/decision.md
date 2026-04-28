# lightgbm_deeper_frequency_capped

## Hypothesis
The current LightGBM champion may be underfitting capped pure-premium ranking; modestly deeper trees may improve segmentation while staying inside the capped calibration and error gates.

## Candidate Change
LightGBM challenger with slightly deeper frequency and capped-severity trees, retaining L2 regularization and minimum leaf-size controls.

## CV Metric Summary
- Capped pure premium Gini: 0.1826
- Capped pure premium calibration gap: -0.0143
- Capped pure premium MAE: 217.5298
- Raw pure premium Gini: 0.1929
- Raw pure premium calibration gap: -0.0663
- Runtime seconds: 25.916275

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| minimum_capped_gini_gain | False |
| minimum_fold_agreement | False |
| capped_calibration_tolerance | True |
| capped_mae_tolerance | True |
| capped_rmse_tolerance | True |
| raw_gini_not_materially_worse | False |

## Actuarial Interpretation
This remains a research-champion candidate, not an automatic pricing level. The depth increase is deliberately modest and still constrained by minimum leaf sizes and L2 penalties.

## Decision
discard

Gate failures: minimum_capped_gini_gain, minimum_fold_agreement, raw_gini_not_materially_worse

Log truncated: False
