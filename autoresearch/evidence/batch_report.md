# MTPL Autoresearch Batch Report

Baseline evidence has been established through the autoresearch harness.

## Champion History

- Pricing-level champion: `baseline_enhanced_glm_splines`.
- Segmentation/research champion: `lightgbm_regularized_challenger`.
- Baseline run: `20260427_181736_d8ef4b3_baseline_enhanced_glm_splines`.
- Capped pure premium Gini: `0.16840000`.
- Capped pure premium calibration gap: `0.00190000`.
- Capped pure premium MAE: `219.09040000`.
- Raw pure premium Gini: `0.15400000`.
- Runtime: `20.30` seconds.
- New segmentation champion run: `20260427_185953_5a72560_lightgbm_regularized_challenger`.
- Champion capped pure premium Gini: `0.18270000`.
- Champion capped pure premium calibration gap: `-0.01450000`.
- Champion capped pure premium MAE: `217.62450000`.
- Champion raw pure premium Gini: `0.19800000`.
- Champion runtime: `20.15` seconds.

## Near Misses

- `enhanced_glm_driver_car_age_interaction`: held calibration and MAE but missed capped Gini gain and fold agreement.
- `enhanced_glm_power_brand_frequency`: improved raw Gini slightly but failed capped Gini gain.
- `enhanced_glm_region_density_frequency`: preserved calibration and slightly improved capped MAE, but reduced capped and raw pure premium Gini.
- `enhanced_glm_region_density_capped_severity`: crashed because severity-side `DensityBand` levels did not match policy-scoring `DensityBand` levels; do not retry severity `DensityBand` terms without a harness-level factor-level fix.
- `enhanced_glm_driver_car_age_capped_severity`: kept calibration inside tolerance but materially reduced capped pure premium Gini and slightly worsened capped MAE.
- `enhanced_glm_power_brand_capped_severity`: slightly improved capped Gini, calibration, and capped pure premium MAE, but the gains were not material and the capped severity BIC/deviance diagnostics did not support the extra sparse interaction complexity.
- `enhanced_glm_power_brand_frequency_capped`: combined the separate Power:Brand signals and improved raw Gini, but capped Gini fell below baseline while parameter count increased materially.
- `enhanced_glm_component_scalars`: worsened capped calibration, capped MAE, and raw Gini.
- `lightgbm_deeper_frequency_capped`: slightly lowered capped MAE but missed capped Gini gain, failed fold agreement, and reduced raw Gini.
- `lightgbm_flexible_capped_severity`: improved capped Gini to `0.1839` and lowered capped MAE, but did not clear the `+0.005` champion gain gate.
- `lightgbm_aggressive_capped_severity`: improved capped Gini to `0.1856` and lowered capped MAE, but the lift came mainly from fold 3 while folds 1 and 2 were slightly worse than the champion.
- `lightgbm_expanded_regularized_grid`: improved capped MAE and raw calibration versus champion, but capped Gini fell to `0.1820` and fold agreement still failed.

## Next Ideas

- Try translating the LightGBM gain back into a transparent GLM term set.
- Revisit `Power:Brand` capped severity only if paired with a parsimony mechanism or stricter sparse-cell pooling.
- Do not combine sparse `Power:Brand` across multiple GLM components without a pooling or selection mechanism.
- Try a slightly more regularized LightGBM variant to see whether calibration improves without losing the capped Gini gain.
- Try capped-severity-specific stabilization while preserving the LightGBM frequency signal.
- Broad LightGBM grids that include conservative alternatives may optimize MAE/calibration at the expense of ranking; require capped Gini to remain the primary segmentation hurdle.
- Avoid isolated frequency-only geographic interactions unless paired with evidence from the LightGBM feature pattern.
- Avoid severity-side `DensityBand` interactions until the immutable R bridge uses one shared density-band reference across frequency and severity scoring frames.
- Avoid further pure capped-severity flexibility unless it improves fold 1 and fold 2, not just fold 3.
