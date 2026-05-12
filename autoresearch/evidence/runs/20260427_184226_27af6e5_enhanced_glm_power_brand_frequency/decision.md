# enhanced_glm_power_brand_frequency

## Hypothesis
Vehicle power may interact with grouped vehicle brand in claim frequency, adding segmentation signal without changing the severity model.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Power:Brand to the frequency component only.

## CV Metric Summary
- Capped pure premium Gini: 0.1669
- Capped pure premium calibration gap: 0.002
- Capped pure premium MAE: 219.0905
- Raw pure premium Gini: 0.1565
- Raw pure premium calibration gap: 0.003
- Runtime seconds: 97.226344

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
Power and brand are standard vehicle risk dimensions. A frequency-only interaction is transparent but should be rejected if sparse classes create unstable relativity movement.

## Decision
discard

Gate failures: minimum_capped_gini_gain

Log truncated: False
