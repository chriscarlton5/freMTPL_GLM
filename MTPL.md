# freMTPL Data Notes

The `freMTPLfreq` and `freMTPLsev` datasets describe French motor third-party liability policies and claims.

## Overview

Risk features are collected for 413,169 motor third-party liability policies, observed mostly over one year. The frequency dataset contains policy-level risk features and claim counts. The severity dataset contains claim amounts keyed by policy ID. Some claim amounts in `freMTPLsev` are fixed according to the French IRSA-IDA claim convention.

## Usage

```r
data(freMTPLfreq)
data(freMTPLsev)
```

## freMTPLfreq

`freMTPLfreq` contains 10 columns:

- `PolicyID`: The policy ID used to link with the claims dataset.
- `ClaimNb`: Number of claims during the exposure period.
- `Exposure`: The exposure period for a policy, in years.
- `Power`: The power of the car.
- `CarAge`: The vehicle age, in years.
- `DriverAge`: The driver age, in years.
- `Brand`: Car brand grouped into:
  - A: Renault Nissan and Citroen
  - B: Volkswagen, Audi, Skoda, and Seat
  - C: Opel, General Motors, and Ford
  - D: Fiat
  - E: Mercedes Chrysler and BMW
  - F: Japanese (except Nissan) and Korean
  - G: Other
- `Gas`: Fuel type, either Diesel or regular.
- `Region`: Policy region in France, based on the 1970-2015 classification.
- `Density`: Number of inhabitants per square kilometer in the city where the driver lives.

## freMTPLsev

`freMTPLsev` contains 2 columns:

- `PolicyID`: The policy ID used to link with the policy dataset.
- `ClaimAmount`: The cost of the claim, observed at a recent valuation date.

## Working Rule

- Do not browse raw CSV files deeply during this project.
- If inspection is necessary, limit it to headers, dimensions, a very small sample, or targeted summaries needed for debugging or model validation.
