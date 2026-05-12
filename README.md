# French MTPL Actuarial Modeling Project

I built this project as an exploratory exercise to 'learn-by-doing' the fundamentals of actuarial modeling and property-and-casualty price modeling. The dataset is the French motor third-party liability (freMTPL) frequency/severity data, and the modeling target is policy-level expected annual loss cost, also called pure premium:

```text
pure premium = expected annual claim frequency * expected claim severity
```

The project starts with a classical frequency/severity GLM, adds a LightGBM challenger, then adapts an autonomous research loop inspired by Andrej Karpathy's `autoresearch` pattern to test whether systematic model iteration could improve the pricing and segmentation results. The answer was yes: the loop found a stronger LightGBM challenger than both the transparent GLM baseline and the initial GBM.

This was a fun side project for educational purposes only. I used this project to learn about GLM/GBM models and halfway through had kind of a wild idea to see if I could adapt current AI-research methods to actuarial modeling in order to improve pricing models autonomously. It appears the answer is yes! 
## Project Goal

The central question was:

> Can an autonomous research harness improve property and casualty pricing models?

The practical goals were to:

- build a basic GLM/GBM as best I could as a non-expert
- estimate expected annual loss cost from frequency and severity components
- compare a transparent GLM against a more flexible LightGBM
- evaluate ranking, calibration, and error rather than a single leaderboard metric
- use GBM feature importance, partial dependence plots, and interaction summaries to understand what the challenger learned
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

## What the Autoresearch Loop Changed

The autoresearch loop did not simply discover that "GBM beats GLM." The initial LightGBM already improved segmentation over the transparent GLM. The loop improved the GBM itself by testing more regularized and more randomized LightGBM configurations.

The initial kept GBM, `lightgbm_regularized_challenger`, used constrained leaf counts and moderate L2 penalties. Its hypothesis was that a restrained LightGBM could improve capped pure-premium ranking while preserving calibration and error stability. The final pricing challenger, `lightgbm_best_191`, pushed a "high randomization" hypothesis: lower feature and bagging fractions, stronger frequency L2 regularization, constrained leaf counts, higher minimum leaf sizes, and a longer boosting budget.

That change made the model better at ranking risk without creating an unacceptable calibration tradeoff. Capped pure-premium Gini improved from `0.1827` to `0.1909`, raw pure-premium Gini improved from `0.1980` to `0.2140`, and absolute capped calibration error improved from `1.45%` to `0.97%`. The fold-level capped Gini also improved in all three folds, which made the result more defensible than a single aggregate lift. The only meaningful tradeoff was capped MAE, which moved from `217.6245` to `218.1074`, about a `0.22%` deterioration.

The winning GBM was still trained in R. Python orchestrated the autonomous research loop: it wrote candidate specs, launched runs, applied gates, and recorded evidence. The actual GLM and LightGBM training stayed in the R workflow through `autoresearch/r/candidate_runner.R` and `autoresearch/r/harness.R`, preserving consistency with the original actuarial modeling code.

## Actuarial Interpretation

This side project tested whether an automated actuarial research harness could improve pure-premium pricing beyond a transparent GLM and an initial LightGBM challenger. The answer is yes. Our winning LightGBM was produced 100% autonomously and improved capped pure-premium Gini from 0.1684 for the GLM baseline to 0.1909, a 13.4% relative lift, while also improving capped MAE from 219.09 to 218.11. Importantly, the harness also improved on the earlier GBM challenger: capped Gini rose from 0.1827 to 0.1909, raw pure-premium Gini rose from 0.1980 to 0.2140, and absolute capped calibration error improved from 1.45% to 0.97%. The only tradeoff was a very small MAE deterioration versus the first GBM, about 0.22%, which I consider acceptable because the final model delivered stronger risk ranking and better calibration while passing predefined gates. My conclusion is that GBMs added real segmentation value, but the actuarial discipline came from treating them as challengers subject to calibration, stability, and interpretability constraints rather than simply selecting the highest-scoring black-box model.

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
