"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_frequency_capped",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Power:Brand to frequency and capped severity."
    ),
    "hypothesis": (
        "Power:Brand frequency improved raw ranking while Power:Brand capped "
        "severity slightly improved capped MAE and calibration. Combining the "
        "two transparent terms may produce enough stable pure premium movement "
        "to clear the pricing gate."
    ),
    "actuarial_rationale": (
        "Vehicle power and brand are standard actuarial rating dimensions. "
        "The combined term set is still transparent, but it adds many sparse "
        "cells, so it must improve ranking or error enough to justify its "
        "complexity."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
    "severity": {
        "use_splines": True,
        "interactions": [],
    },
    "capped_severity": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
    "calibration": {
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
