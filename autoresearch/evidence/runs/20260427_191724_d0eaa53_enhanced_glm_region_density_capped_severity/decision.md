# enhanced_glm_region_density_capped_severity

## Hypothesis
The capped-severity GBM importance suggests regional density signal may belong in capped severity rather than frequency. A capped-only interaction may improve stable pure premium ranking without disturbing frequency calibration.

## Candidate Change
Enhanced GLM using natural splines for DriverAge, CarAge, and logDensity in frequency, raw severity, and capped severity; adds Region:DensityBand to the capped severity component only.

## CV Metric Summary
- Capped pure premium Gini: None
- Capped pure premium calibration gap: None
- Capped pure premium MAE: None
- Raw pure premium Gini: None
- Raw pure premium calibration gap: None
- Runtime seconds: 9.341545

## Gate Results
| Gate | Passed |
| --- | --- |

## Actuarial Interpretation
Capped severity is a stability view, so this tests the geography signal where tail noise is reduced. The interaction remains explicit and reviewable, but it should be rejected if it creates sparse-cell relativity movement without cross-fold metric support.

## Decision
crash

Gate failures: candidate crashed

Log truncated: False
