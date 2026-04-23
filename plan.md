# Fast MTPL GLM Project Plan Using Mostly Stock R

## Summary

- Build a tight v1 in `R` using mostly base or stock functionality: `read.csv`, `merge`, base factor handling, `glm`, `predict`, and base plotting or diagnostics.
- Main deliverable is one `R Markdown` analysis that reads the MTPL files, fits a frequency GLM and severity GLM, combines them into a pure premium view, and explains the result in business-friendly language.
- Working rule: do not browse raw CSVs deeply. Only inspect headers, dimensions, a very small sample, and targeted summaries when needed.

## Implementation Changes

- Environment or setup:
  - Confirm `R` is runnable on this machine and install only the minimum needed to render `R Markdown`.
  - Prefer base `stats` and base plotting over tidyverse or heavier modeling packages unless a specific gap forces otherwise.
- Data prep:
  - Add the supplied dataset description to `MTPL.md`.
  - Read `freMTPLfreq.csv` and `freMTPLsev.csv` with base `R`.
  - Keep policy-level data in the frequency table and join claim amounts to policy features with base `merge` for severity modeling.
  - Apply only light cleanup: key-field sanity checks, positive-exposure enforcement, positive-claim filtering for severity, and simple transform consideration for `Density` if diagnostics justify it.
  - Keep feature treatment simple and believable: categorical factors as factors, continuous variables mostly continuous unless a very clear binning reason appears.
- Modeling:
  - Create one fixed train or holdout split at the policy level so claims from the same policy never leak across sets.
  - Frequency: Poisson GLM with log link and `offset(log(Exposure))`.
  - Severity: Gamma GLM with log link on positive claim amounts.
  - Pure premium: expected frequency times expected severity, reported as expected claim cost per policy-year.
  - Use only modest comparisons: dispersion check for frequency and core residual or influence checks for both models. Do not broaden scope unless results clearly demand it.
- Reporting:
  - Keep one notebook-centered narrative with a short technical memo style.
  - Show a few high-signal outputs only: data sanity summary, model formulas, coefficient interpretation at a high level, holdout performance summary, pure premium by selected segments, and a few example policy profiles.
  - Include brief interview talking points and a short limitations or governance section.

## Stop-And-Ask Rules

- Stop and ask before proceeding if `R` is not available or package setup becomes nontrivial.
- Stop and ask if the frequency model shows material overdispersion or obviously unstable coefficients.
- Stop and ask if the severity model is dominated by extreme claims, has implausible fitted behavior, or suggests the baseline Gamma setup is not credible.
- Stop and ask if the holdout results materially conflict with the in-sample story or if any data join or check looks suspicious.
- Otherwise keep moving and only surface concise progress updates.

## Test Plan

- Confirm the notebook renders end-to-end on this machine.
- Verify policy or claim join logic, train or holdout separation, and exposure handling.
- Check frequency dispersion and basic residual behavior.
- Check severity residual or influence behavior and sensitivity to large losses.
- Confirm the final output gives a credible pure premium story that is easy to explain to a non-technical audience.

## Assumptions

- Stock or base `R` is preferred whenever possible. External packages are acceptable only when they are necessary for notebook rendering or a clearly justified gap.
- This remains a narrow v1 intended to be finishable quickly, not a full actuarial pricing study.
- If anything looks materially off, implementation pauses and questions come back to the user before scope expands or modeling choices change.
