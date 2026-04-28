"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_region_density_frequency",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Region:DensityBand to the frequency component only."
    ),
    "hypothesis": (
        "Regional density interaction may recover transparent frequency "
        "segmentation that the LightGBM found, while preserving the pricing "
        "GLM's strong capped pure premium calibration."
    ),
    "actuarial_rationale": (
        "Territory and density are plausible exposure/risk modifiers, but the "
        "term is kept in frequency only because claim count is the more stable "
        "component for geographic segmentation. The interaction remains "
        "auditable as a banded GLM term."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": ["Region:DensityBand"],
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
