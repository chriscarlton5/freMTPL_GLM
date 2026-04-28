"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_agefreq_powerbrand_dual_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in all components; adds DriverAgeBand:CarAgeBand to "
        "frequency and Power:Brand to raw and capped severity."
    ),
    "hypothesis": (
        "The strongest transparent frequency and severity near misses may be "
        "complementary: age-car segmentation captures claim propensity while "
        "Power:Brand captures repair-cost severity."
    ),
    "actuarial_rationale": (
        "Driver age, car age, power, and brand are plausible rating dimensions. "
        "The combined interaction set remains interpretable but must overcome a "
        "high parsimony burden and sparse-cell stability risk."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": ["DriverAgeBand:CarAgeBand"],
    },
    "severity": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
    "capped_severity": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
