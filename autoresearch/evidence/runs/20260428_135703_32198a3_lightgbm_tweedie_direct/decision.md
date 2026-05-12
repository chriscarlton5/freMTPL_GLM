# lightgbm_tweedie_direct

## Hypothesis
Traditional freq x sev separate is suboptimal. Tweedie directly optimizes pure premium - standard actuarial practice. Target is E[N] * E[S].

## Candidate Change
NEW HYPOTHESIS: Use Tweedie objective (variance_power=1.5) to optimize pure premium directly. Actuarially better than frequency x severity separate models.

## CV Metric Summary
- Capped pure premium Gini: 0.1851
- Capped pure premium calibration gap: -0.0098
- Capped pure premium MAE: 218.0687
- Raw pure premium Gini: 0.2004
- Raw pure premium calibration gap: -0.0494
- Runtime seconds: 17.931466

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
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Tweedie is actuarially preferred for pure premium. Combines frequency and severity into single objective. Standard practice in insurance pricing.

## Decision
keep

Gate failures: none

Log truncated: False
