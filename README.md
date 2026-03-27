# COM407 Applied AI

Practical course workspace for COM407 (Applied AI), organised by teaching week.

This repository contains notebooks, datasets, model checkpoints, and outputs used across the module.

## Quick Start

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Open the relevant weekly notebook in your IDE/Jupyter environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you run notebooks outside an IDE with built-in notebook support, install and launch Jupyter:

```bash
pip install jupyterlab
jupyter lab
```

## Repository Layout

```text
COM407-AppliedAI/
|- Folder_Setup.ipynb
|- requirements.txt
|- utils/
|  |- configTest.py
|- week_1/ ... week_12/
|  |- assets/   (input data, starter files, model metadata)
|  |- outputs/  (generated predictions, checkpoints, saved artifacts)
```

## Week-by-Week Structure

- `week_1/`: Introduction and baseline framing.
- `week_2/`: Neural network warm-up and model-from-scratch exercises.
- `week_3/`: Data pipelines and tokenisation (including mini news splits/tokenized datasets).
- `week_4/`: Dataset recap and structured/tabular workflows.
- `week_5/`: Transformer foundations.
- `week_6/`: Transformer exercises and manual inference outputs.
- `week_7/`: AG News lab and fine-tuning experiments.
- `week_8/` to `week_12/`: Later-week assets and outputs.

## Working Conventions

- Keep source notebooks in the relevant `week_x/` folder.
- Place input files in `week_x/assets/`.
- Save generated files to `week_x/outputs/`.
- Avoid overwriting raw datasets; create derived files in `outputs/` where possible.
- Keep notebook runs reproducible (set seeds when needed and document major decisions in markdown cells).

## Typical Weekly Workflow

1. Open that week's notebook(s).
2. Confirm dependencies are installed in your active environment.
3. Run cells top-to-bottom once to validate baseline execution.
4. Iterate on experiments and save artifacts to `outputs/`.
5. Record key findings in notebook markdown cells (or a week-level README if needed).

## Dependencies

Main packages are defined in `requirements.txt`, including:

- `transformers`
- `torch`
- `tensorflow`
- `datasets`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Install/update at any time with:

```bash
pip install -r requirements.txt
```

## Notes

- Some folders (for example checkpoints in `week_7/assets/`) can be large.
- If notebooks fail due to missing optional tooling, install the missing package in your active environment and rerun.
- Keep path usage relative to the project root where possible for portability.

