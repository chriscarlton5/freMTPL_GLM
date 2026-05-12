# enhanced_glm_driver_car_age_interaction

## Hypothesis
A transparent young-driver by vehicle-age interaction may improve frequency risk segmentation without compromising capped pure premium stability.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds DriverAgeBand:CarAgeBand to the frequency component only.

## CV Metric Summary
- Capped pure premium Gini: 0.1671
- Capped pure premium calibration gap: 0.0019
- Capped pure premium MAE: 219.0808
- Raw pure premium Gini: 0.1556
- Raw pure premium calibration gap: 0.0028
- Runtime seconds: 34.003521

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
| raw_gini_not_materially_worse | True |

## Actuarial Interpretation
Driver age and vehicle age are standard actuarial rating dimensions. A limited banded interaction is easier to defend than a black-box effect, but should be rejected if sparse cells reduce stability.

## Decision
discard

Gate failures: minimum_capped_gini_gain, minimum_fold_agreement

Log truncated: False
