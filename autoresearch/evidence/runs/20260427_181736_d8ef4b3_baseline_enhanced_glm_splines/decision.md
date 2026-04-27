# baseline_enhanced_glm_splines

## Hypothesis
The current report's enhanced GLM structure is the right starting champion for transparent actuarial segmentation.

## Candidate Change
Baseline transparent enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; no interactions or calibration scalars.

## CV Metric Summary
- Capped pure premium Gini: 0.1684
- Capped pure premium calibration gap: 0.0019
- Capped pure premium MAE: 219.0904
- Raw pure premium Gini: 0.154
- Raw pure premium calibration gap: 0.0028
- Runtime seconds: 20.30181

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |

## Actuarial Interpretation
Natural splines allow smooth nonlinear age and density effects while remaining reviewable, parsimonious, and defensible compared with a direct black-box pricing level.

## Decision
keep

Gate failures: none

Log truncated: False
