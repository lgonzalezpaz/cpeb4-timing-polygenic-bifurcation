# Developmental timing and polygenic background bifurcate CPEB4 microexon 4 mis-splicing between autism and schizophrenia

Code, processed data, results and manuscript files for the study of how neurodevelopmental timing
(early synaptogenesis versus adolescent synaptic pruning) and baseline polygenic risk determine whether
*CPEB4* microexon 4 (me4) mis-splicing leads to autism spectrum disorder (ASD) or schizophrenia (SCZ).

## Overview

The Condensate–Timing–Liability (CTL) framework has four scales:

1. **Scale 1** – heterotypic-buffering biophysics and condensate-locking kinetics, calibrated to published
   CPEB4 phase-separation source data (Eqs. 1–6).
2. **Scale 2** – human prefrontal synaptic density driven by synaptogenesis and activity-coupled pruning (Eq. 7).
3. **Scale 3** – correlated ASD/SCZ polygenic liabilities and developmental vulnerability kernels (Eqs. 8–13).
4. **Scale 4** – conditional induction and splice-switching oligonucleotide (SSO) rescue protocols (Eqs. 14–16).

Empirical validation uses UniProt, Garcia-Cabau et al. (2025) source data, Parras et al. (2018) CPEB4 targets,
BrainSpan, PsychENCODE, Gandal et al. (2018), SFARI Gene, Fu et al. (2022), SCHEMA, Open Targets, SynGO and
Ensembl BioMart.

## Repository layout

```
src/        analysis pipeline (01–08), manuscript content, OMML equations, inline-markup parser
tests/      data-integrity, mathematical-reproducibility and manuscript audits
data/raw/   download provenance (SHA-256); large raw files are re-downloaded by src/01
data/processed/  harmonized inputs used by all analyses
results/    numerical outputs (JSON/CSV)
figures/    600-dpi PNG plus vector PDF/SVG figures
manuscript/ DOCX/Markdown manuscript, supplementary material, title page, cover letter, file list
```

## Reproduction

```bash
conda env create -f environment.yml      # or: pip install -r requirements.txt
conda activate cpeb4-ctl
python run_all.py                        # full pipeline (downloads raw data, ~network required)
python run_all.py --skip-fetch           # reuse data/processed, re-run analyses, figures and manuscript
python run_all.py --verify-only          # run the test suites only
```

All stochastic steps use fixed seeds (`SEED = 42` for bioinformatics; `SEED = 20261119` for modelling).

## Tests

```bash
python tests/test_step1_data_integrity.py
python -m unittest tests.test_math_reproducibility -v
python src/06_verify_references.py --verify-only
python tests/audit_manuscript.py
```

## Licence and citation

Code is released under the MIT License (see `LICENSE`). Please cite the article and this archive
(see `CITATION.cff`). Third-party datasets remain subject to their original terms of use.
