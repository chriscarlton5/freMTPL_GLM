# French MTPL Actuarial Modeling Project

This project builds a fast, credible first-pass actuarial pricing study from the French MTPL data. It starts with a classical GLM frequency/severity model, then adds a LightGBM challenger to test whether gradient boosting improves risk segmentation, calibration, or interaction discovery.

The core actuarial target is annual expected loss cost:

```text
pure premium = expected annual claim frequency * expected claim severity
```

## Deliverables

- [MTPL.md](C:\Users\mbcar\OneDrive\Desktop\french\MTPL.md): dataset notes and project working rule for data inspection.
- [glmplan.md](C:\Users\mbcar\OneDrive\Desktop\french\glmplan.md): original GLM implementation plan and stop conditions.
- [GBMPlan.md](C:\Users\mbcar\OneDrive\Desktop\french\GBMPlan.md): LightGBM comparison plan centered on pure premium and risk segmentation.
- `mtpl_glm_analysis.R`: base-`R` workflow for loading data, fitting models, and producing summary objects.
- `mtpl_glm_report.Rmd`: notebook-style report that explains the project and renders the model results.
- `mtpl_gbm_analysis.R`: LightGBM challenger workflow and GLM-vs-GBM comparison objects.
- `mtpl_gbm_glm_synthesis.R`: GBM-first synthesis workflow that converts selected GBM learnings into an enhanced transparent GLM.
- `mtpl_gbm_report.Rmd`: notebook-style report comparing GLM, LightGBM, and the GBM-informed enhanced GLM.
- `docs/glm.html`: preserved static GLM walkthrough.
- `docs/index.html`: GitHub Pages-ready static GBM comparison walkthrough.

## Modeling Scope

- GLM benchmark:
  - Frequency: Poisson GLM with an exposure offset.
  - Severity: Gamma GLM on positive claim amounts.
  - Pure premium: annual expected frequency times expected claim severity.
- LightGBM challenger:
  - Frequency: Poisson objective on annual claim frequency, weighted by exposure.
  - Severity: Gamma objective on raw positive claim amounts.
  - Severity sensitivity: Gamma objective on 99.5% capped claim amounts.
  - Pure premium: derived from the frequency and severity predictions.
- GBM-informed GLM synthesis:
  - Run the full LightGBM analysis before enhancing the GLM.
  - Test GBM-inspired splines and interactions on the holdout set.
  - Retain only transparent terms that improve the relevant holdout metric without unacceptable calibration deterioration.

## Project Rules

- Prefer stock `R` functionality for the GLM baseline and minimal external packages for the GBM comparison.
- Avoid deep raw-CSV browsing; use only targeted summaries and tiny samples if inspection is necessary.
- Stop and review if diagnostics or holdout behavior look materially off.
- Treat GLM as the benchmark and GBM as the challenger. The goal is credible expected loss cost estimation and risk segmentation, not simply the lowest error metric.

## GitHub Pages

This project is set up for the simplest static deployment path on GitHub Pages.

1. Create a GitHub repository and push this folder to it.
2. In GitHub, open `Settings` -> `Pages`.
3. Under `Build and deployment`, choose `Deploy from a branch`.
4. Select your main branch and the `/docs` folder.
5. Save the settings and wait for GitHub Pages to publish the site.

The published site will serve `docs/index.html`, which is the rendered GLM-vs-LightGBM walkthrough. The original GLM-only walkthrough is preserved at `docs/glm.html`.

If you rerender the GBM report later, copy the new `mtpl_gbm_report.html` over `docs/index.html` before pushing. If you rerender the GLM report later, copy the new `mtpl_glm_report.html` over `docs/glm.html`.
