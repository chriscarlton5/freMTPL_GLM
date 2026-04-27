"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_frequency",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, "
        "CarAge, and logDensity in frequency, raw severity, and capped severity; "
        "adds Power:Brand to the frequency component only."
    ),
    "hypothesis": (
        "Vehicle power may interact with grouped vehicle brand in claim frequency, "
        "adding segmentation signal without changing the severity model."
    ),
    "actuarial_rationale": (
        "Power and brand are standard vehicle risk dimensions. A frequency-only "
        "interaction is transparent but should be rejected if sparse classes create "
        "unstable relativity movement."
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
        "interactions": [],
    },
    "calibration": {
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
