# AI Agent Instructions for kulangiev.github.io

This repository hosts a static GitHub Pages portfolio for B. B. Kulangiev's research on emergent gravity, electromagnetism, and cosmology from a logarithmic superfluid vacuum framework.

## Project Overview
- **Purpose**: Personal research website with 12+ LaTeX papers and Python simulation scripts
- **Structure**: Flat organization with `papers/paper_N/` folders containing `.tex` files and figure generation code
- **Deployment**: Static HTML via GitHub Pages (no build system)
- **Overarching Aim**: Develop hydrodynamic deterministic foundations of physics, deriving all of quantum mechanics (QM), gravity, and electromagnetism (EM) from underlying deterministic fluid dynamics

## Key Conventions
- **Papers**: LaTeX documents in `papers/paper_N/paper_N.tex`; some include Python scripts (`paperN_figures.py`) for numerical simulations and matplotlib figures
- **Website**: Single `index.html` with embedded CSS; manually curated paper listings and results
- **Physics Context**: All work derives from a relativistic logarithmic superfluid vacuum model; comments reference equations and paper sections
- **Code Style**: Verbose variable names, physics-first documentation, NumPy/matplotlib for simulations

## Common Tasks
- **Add Paper**: Create `papers/paper_N/` folder, add `.tex` file, update `index.html` navigation and paper list
- **Generate Figures**: Run Python scripts in paper folders to produce PDF/PNG outputs
- **Update Portfolio**: Edit `index.html` for new results, predictions, or paper statuses

## Pitfalls
- Manual synchronization required between papers and website
- Physics domain knowledge needed for code changes
- No automated LaTeX compilation or CI/CD

See [README.md](README.md) and [index.html](index.html) for more details.