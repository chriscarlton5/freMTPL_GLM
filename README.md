# French MTPL GLM Project

This project builds a fast, credible first-pass actuarial pricing study from the French MTPL data using mostly stock `R`.

## Deliverables

- [MTPL.md](C:\Users\mbcar\OneDrive\Desktop\french\MTPL.md): dataset notes and project working rule for data inspection.
- [plan.md](C:\Users\mbcar\OneDrive\Desktop\french\plan.md): implementation plan and stop conditions.
- `mtpl_glm_analysis.R`: base-`R` workflow for loading data, fitting models, and producing summary objects.
- `mtpl_glm_report.Rmd`: notebook-style report that explains the project and renders the model results.
- `docs/index.html`: GitHub Pages-ready static version of the walkthrough.

## Modeling Scope

- Frequency model: Poisson GLM with an exposure offset.
- Severity model: Gamma GLM on positive claim amounts.
- Pure premium: annual expected frequency times expected claim severity.

## Project Rules

- Prefer stock `R` functionality wherever possible.
- Avoid deep raw-CSV browsing; use only targeted summaries and tiny samples if inspection is necessary.
- Stop and review if diagnostics or holdout behavior look materially off.

## GitHub Pages

This project is set up for the simplest static deployment path on GitHub Pages.

1. Create a GitHub repository and push this folder to it.
2. In GitHub, open `Settings` -> `Pages`.
3. Under `Build and deployment`, choose `Deploy from a branch`.
4. Select your main branch and the `/docs` folder.
5. Save the settings and wait for GitHub Pages to publish the site.

The published site will serve `docs/index.html`, which is the rendered MTPL walkthrough.

If you rerender the report later, copy the new `mtpl_glm_report.html` over `docs/index.html` before pushing.
