"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_capped_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Power:Brand to the capped severity component only."
    ),
    "hypothesis": (
        "Vehicle power and brand were material GBM severity features. A capped "
        "severity interaction may capture vehicle repair-cost segmentation "
        "while avoiding raw severity tail amplification."
    ),
    "actuarial_rationale": (
        "Power and brand can plausibly affect repair costs, but this term has "
        "sparse cells. It is acceptable only if capped pure premium ranking, "
        "error, and fold agreement support the added complexity."
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
        "interactions": ["Power:Brand"],
    },
    "calibration": {
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
