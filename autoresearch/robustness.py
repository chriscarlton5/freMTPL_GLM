"""Run locked post-selection robustness validation for the MTPL autoresearch champions."""

from __future__ import annotations

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
AUTORESEARCH_DIR = Path(__file__).resolve().parent
ROBUSTNESS_DIR = AUTORESEARCH_DIR / "evidence" / "robustness"
R_SCRIPT = AUTORESEARCH_DIR / "r" / "robustness_runner.R"


def resolve_rscript() -> str:
    env_path = os.environ.get("RSCRIPT") or os.environ.get("R_SCRIPT")
    candidates = [
        env_path,
        shutil.which("Rscript"),
        r"C:\Program Files\R\R-4.5.3\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.2\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.1\bin\Rscript.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    raise RuntimeError("Could not find Rscript. Set RSCRIPT to the full Rscript.exe path.")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = ROBUSTNESS_DIR / timestamp
    output_dir.mkdir(parents=True, exist_ok=False)

    command = [
        resolve_rscript(),
        str(R_SCRIPT),
        str(output_dir),
        str(REPO_ROOT),
    ]
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    log_text = ""
    if completed.stdout:
        log_text += "[stdout]\n" + completed.stdout
        if not completed.stdout.endswith("\n"):
            log_text += "\n"
    if completed.stderr:
        log_text += "[stderr]\n" + completed.stderr
        if not completed.stderr.endswith("\n"):
            log_text += "\n"
    (output_dir / "run.log").write_text(log_text, encoding="utf-8")

    if completed.returncode != 0:
        raise SystemExit(
            f"Robustness validation failed with exit code {completed.returncode}. "
            f"See {output_dir / 'run.log'}"
        )

    latest_dir = ROBUSTNESS_DIR / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    for path in latest_dir.iterdir():
        if path.is_file():
            path.unlink()
    for path in output_dir.iterdir():
        if path.is_file():
            shutil.copy2(path, latest_dir / path.name)

    print(f"robustness_dir: {output_dir.relative_to(REPO_ROOT)}")
    print(f"latest_report: {(latest_dir / 'robustness_report.md').relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
