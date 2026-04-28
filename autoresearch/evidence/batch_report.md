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
- `enhanced_glm_component_scalars`: worsened capped calibration, capped MAE, and raw Gini.
- `lightgbm_deeper_frequency_capped`: slightly lowered capped MAE but missed capped Gini gain, failed fold agreement, and reduced raw Gini.

## Next Ideas

- Try translating the LightGBM gain back into a transparent GLM term set.
- Try a slightly more regularized LightGBM variant to see whether calibration improves without losing the capped Gini gain.
- Try capped-severity-specific stabilization while preserving the LightGBM frequency signal.
