# French MTPL Actuarial Modeling Project

I built this project as an exploratory exercise to learn the fundamentals of actuarial modeling and property-and-casualty price modeling. The dataset is the French motor third-party liability (MTPL) frequency/severity data, and the modeling target is policy-level expected annual loss cost, also called pure premium:

```text
pure premium = expected annual claim frequency * expected claim severity
```

The project starts with a classical frequency/severity GLM, adds a LightGBM challenger, then adapts an autonomous research loop inspired by Andrej Karpathy's `autoresearch` pattern to test whether systematic model iteration could improve the pricing and segmentation results. The answer was yes: the loop found a stronger LightGBM challenger than both the transparent GLM baseline and the initial GBM.

This is a side-project pricing study, not a production rate filing. I use the project to demonstrate modeling judgment, validation discipline, and the tradeoff between transparent actuarial models and higher-performing machine-learning challengers.

## Project Goal

The central question was:

> Can a transparent actuarial GLM and a GBM challenger estimate expected annual loss cost credibly, and can an autonomous research harness improve the challenger without losing calibration or governance discipline?

The practical goals were to:

- estimate expected annual loss cost from frequency and severity components,
- compare a transparent GLM against a more flexible LightGBM,
- evaluate ranking, calibration, and error rather than a single leaderboard metric,
- use GBM feature importance, partial dependence plots, and interaction summaries to understand what the challenger learned,
- test whether an autonomous research loop could improve the baseline modeling results while preserving an auditable evidence trail.

## Data and Actuarial Target

The project uses the French MTPL frequency and severity datasets:

- `freMTPLfreq`: policy-level exposure, claim counts, and rating variables such as driver age, vehicle age, vehicle power, brand, fuel type, region, and population density.
- `freMTPLsev`: claim-level amounts linked back to policies by `PolicyID`.

The actuarial target is expected annual pure premium:

```text
expected annual pure premium = expected annual claim frequency * expected claim severity
```

The baseline GLM uses a Poisson frequency model with an exposure offset and Gamma severity models on positive claim amounts. The LightGBM challenger mirrors that structure with a Poisson objective for frequency and Gamma objectives for raw and capped severity. The capped severity view uses a 99.5% severity cap as a stability check on body-of-loss behavior; raw pure premium remains the main business target.

## Modeling Workflow

The project has three modeling layers.

First, I built a transparent GLM benchmark. This is the actuarially familiar starting point: easy to explain, easy to inspect, and strong for aggregate calibration.

Second, I trained a LightGBM challenger to test whether a more flexible model could improve risk segmentation. The GBM was evaluated on the same frequency/severity structure as the GLM, with pure premium derived from the component predictions rather than modeled directly.

Third, I used the GBM as a diagnostic tool for a GBM-informed GLM synthesis. The report tests splines and candidate interactions suggested by the boosted model, but retains only transparent terms that improve validation metrics without unacceptable calibration deterioration.

Throughout the project, I treated Gini, calibration, MAE, decile lift, leakage checks, and finite/nonnegative predictions as complementary diagnostics. The goal was not simply to make the most complex model win; it was to understand whether the extra complexity created actuarially useful signal.

## Autoresearch Experiment

After building the initial GLM and GBM workflows, I adapted an autonomous research loop inspired by Karpathy's `autoresearch` framework. In this repo, Python orchestrates the loop while R remains the source of truth for the actuarial modeling code, feature treatment, splits, and metrics.

The harness lets an agent propose incremental candidate changes, runs each candidate through the same validation workflow, applies hard gates, and records an auditable evidence trail. Each run stores a candidate spec, fold metrics, aggregate metrics, decision memo, and a row in `autoresearch/evidence/results.tsv`.

The key governance idea was to make autonomous experimentation behave more like disciplined actuarial research: no policy leakage, stable validation, calibrated loss-cost behavior, defensible model changes, and tracked decisions.

## Results

The autoresearch loop improved the GBM challenger, not merely the GLM comparison. The selected final LightGBM produced stronger ranking than the initial GBM while also improving absolute capped calibration error.

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped calibration gap |
| --- | --- | ---: | ---: | ---: | ---: |
| Enhanced GLM splines | Transparent baseline | `0.1684` | `0.1540` | `219.0904` | `+0.19%` |
| Regularized LightGBM | Initial GBM challenger | `0.1827` | `0.1980` | `217.6245` | `-1.45%` |
| Autoresearch LightGBM | Final pricing challenger | `0.1909` | `0.2140` | `218.1074` | `-0.97%` |

Compared with the GLM baseline, the final LightGBM improved capped pure-premium Gini from `0.1684` to `0.1909`, raw pure-premium Gini from `0.1540` to `0.2140`, and capped pure-premium MAE from `219.0904` to `218.1074`.

Compared with the initial GBM, the final LightGBM improved capped pure-premium Gini from `0.1827` to `0.1909`, raw pure-premium Gini from `0.1980` to `0.2140`, and absolute capped calibration error from `1.45%` to `0.97%`. The main tradeoff was a small capped MAE deterioration versus the initial GBM, from `217.6245` to `218.1074`, or about `0.22%`. I consider that acceptable in this research context because the final model delivered stronger ranking and better calibration while passing the harness gates.

The source of truth for these results is `autoresearch/evidence/results.tsv`, with selected champions summarized in `autoresearch/evidence/champions.json`.

## Actuarial Interpretation

My conclusion is that GBM added real segmentation value. The GLM remained the clean transparent benchmark, but the LightGBM challenger was better at ranking policies by observed loss cost. The autoresearch loop then found a stronger GBM candidate than the initial hand-built challenger.

That does not mean the final GBM is automatically a filed pricing model. A production filing would require broader governance: explainability review, proxy-variable review, stability testing, reasonableness checks, and business signoff. This repo includes baseline explainability through the GLM comparison, feature importance, partial dependence plots, interaction summaries, and decile-level calibration/lift diagnostics, but it remains an exploratory project.

The strongest story is that the project moved from classical actuarial modeling, to GBM challenger modeling, to autonomous model research, while keeping the analysis grounded in expected loss cost, calibration, ranking, and transparent evidence.

## Repository Guide

- [MTPL.md](MTPL.md): dataset notes and project working rule for data inspection.
- [glmplan.md](glmplan.md): original GLM implementation plan and stop conditions.
- [GBMPlan.md](GBMPlan.md): LightGBM comparison plan centered on pure premium and risk segmentation.
- `mtpl_glm_analysis.R`: base-`R` workflow for loading data, fitting GLM frequency/severity models, and producing summary objects.
- `mtpl_glm_report.Rmd`: notebook-style GLM report.
- `mtpl_gbm_analysis.R`: LightGBM challenger workflow and GLM-vs-GBM comparison objects.
- `mtpl_gbm_glm_synthesis.R`: GBM-first synthesis workflow that converts selected GBM learnings into enhanced transparent GLM terms.
- `mtpl_gbm_report.Rmd`: notebook-style report comparing GLM, LightGBM, and the GBM-informed enhanced GLM.
- `autoresearch/`: autonomous research harness, candidate runner, operating manual, and tracked evidence.
- `docs/glm.html`: preserved static GLM walkthrough.
- `docs/index.html`: GitHub Pages-ready static GBM comparison walkthrough.

## GitHub Pages

This project is set up for the simplest static deployment path on GitHub Pages.

1. Create a GitHub repository and push this folder to it.
2. In GitHub, open `Settings` -> `Pages`.
3. Under `Build and deployment`, choose `Deploy from a branch`.
4. Select your main branch and the `/docs` folder.
5. Save the settings and wait for GitHub Pages to publish the site.

The published site will serve `docs/index.html`, which is the rendered GLM-vs-LightGBM walkthrough. The original GLM-only walkthrough is preserved at `docs/glm.html`.

If you rerender the GBM report later, copy the new `mtpl_gbm_report.html` over `docs/index.html` before pushing. If you rerender the GLM report later, copy the new `mtpl_glm_report.html` over `docs/glm.html`.
