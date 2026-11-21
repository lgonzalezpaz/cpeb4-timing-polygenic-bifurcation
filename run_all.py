#!/usr/bin/env python3
"""Deterministic end-to-end runner for the CPEB4 CTL pipeline.

python run_all.py                 # full pipeline including data download
python run_all.py --skip-fetch    # reuse data/processed
python run_all.py --verify-only   # tests only
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIPELINE = [
    ["src/01_fetch_and_harmonize_data.py"],
    ["src/02_bioinformatics_validation.py"],
    ["src/03_biophysical_calibration.py"],
    ["src/04_multiscale_ctl_model.py"],
    ["src/05_sensitivity_and_cohort.py"],
    ["src/06_verify_references.py", "--verify-only"],
    ["src/07_generate_figures.py", "--figs", "all"],
    ["src/08_build_manuscript_and_package.py", "--no-zip"],
]
TESTS = [
    ["tests/test_step1_data_integrity.py"],
    ["-m", "unittest", "tests.test_math_reproducibility", "-v"],
    ["tests/audit_manuscript.py"],
]


def run(args):
    print("\n>>> python " + " ".join(args), flush=True)
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-fetch", action="store_true")
    ap.add_argument("--verify-only", action="store_true")
    a = ap.parse_args()
    if not a.verify_only:
        for step in PIPELINE:
            if a.skip_fetch and step[0].startswith("src/01_"):
                continue
            run(step)
    for t in TESTS:
        run(t)
    print("\nAll steps completed successfully.")


if __name__ == "__main__":
    main()
