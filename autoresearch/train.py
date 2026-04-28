"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_driver_car_age_capped_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "DriverAgeBand:CarAgeBand to the capped severity component only."
    ),
    "hypothesis": (
        "The GBM interaction review showed large age-by-vehicle-age pure "
        "premium differences. Putting this term in capped severity may improve "
        "stable loss-cost ranking while leaving frequency calibration intact."
    ),
    "actuarial_rationale": (
        "Driver age and vehicle age have plausible claim-size relationships, "
        "but severity is tail-sensitive. This candidate uses the capped target "
        "only and requires cross-fold support before any pricing-level change."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": [],
    },
    "severity": {
        "use_splines": True,
        "interactions": [],
    },
    "capped_severity": {
        "use_splines": True,
        "interactions": ["DriverAgeBand:CarAgeBand"],
    },
    "calibration": {
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
