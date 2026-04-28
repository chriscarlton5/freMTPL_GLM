"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_region_density_capped_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Region:DensityBand to the capped severity component only."
    ),
    "hypothesis": (
        "The capped-severity GBM importance suggests regional density signal "
        "may belong in capped severity rather than frequency. A capped-only "
        "interaction may improve stable pure premium ranking without disturbing "
        "frequency calibration."
    ),
    "actuarial_rationale": (
        "Capped severity is a stability view, so this tests the geography "
        "signal where tail noise is reduced. The interaction remains explicit "
        "and reviewable, but it should be rejected if it creates sparse-cell "
        "relativity movement without cross-fold metric support."
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
        "interactions": ["Region:DensityBand"],
    },
    "calibration": {
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
