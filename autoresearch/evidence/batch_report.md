# MTPL Autoresearch Batch Report

Baseline evidence has been established through the autoresearch harness.

## Champion History

- Pricing-level champion: `baseline_enhanced_glm_splines`.
- Segmentation/research champion: `baseline_enhanced_glm_splines`.
- Baseline run: `20260427_181736_d8ef4b3_baseline_enhanced_glm_splines`.
- Capped pure premium Gini: `0.16840000`.
- Capped pure premium calibration gap: `0.00190000`.
- Capped pure premium MAE: `219.09040000`.
- Raw pure premium Gini: `0.15400000`.
- Runtime: `20.30` seconds.

## Near Misses

None yet.

## Next Ideas

- Try constrained LightGBM tuning only after the baseline evidence is committed.
- Try component-level calibration scalars inside folds and require capped loss-cost stability.
- Try limited, transparent interaction terms only when fold metrics support them.
