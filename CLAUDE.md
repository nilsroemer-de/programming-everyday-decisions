# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Quarto-based educational website for the course "Programming: Everyday Decision-Making Algorithms" at Kühne Logistics University. The course teaches algorithmic thinking concepts (optimal stopping, explore/exploit, caching, scheduling, randomness) while introducing Python programming to business students.

## Build Commands

```bash
# Render the entire website
quarto render

# Preview with live reload
quarto preview

# Render a single file
quarto render lectures/lec_01_optimal_stopping.qmd

# Check Quarto installation (may need QUARTO_CHROMIUM set for PDF export)
QUARTO_CHROMIUM=/Applications/Brave\ Browser.app/Contents/MacOS/Brave quarto check
```

## Python Environment

The project uses `uv` for Python dependency management (Python 3.12):

```bash
# Sync dependencies from pyproject.toml
uv sync

# Run Python scripts
uv run python script.py

# Add a package
uv add package_name
```

Key dependencies: jupyter, jupytext, matplotlib, numpy, pandas

## Repository Structure

- `lectures/` - RevealJS slide decks (`.qmd` files with `format: revealjs`)
- `tutorials/` - Interactive Python tutorials in Quarto format
- `general/` - Course information pages (syllabus, FAQ, installation guide)
- `_quarto.yml` - Main Quarto configuration (website structure, theme, output formats)
- `_brand.yml` - Brand/styling configuration
- `styles.scss` - Custom SCSS styles
- `helpers/` - Conversion scripts (qmd to md, pypercent format)
- `include/` - Reusable Quarto includes (e.g., tutorial_end.qmd)
- `_site/` - Generated output (do not edit)
- `_repo-md/` - Markdown versions of content

## Content Authoring

- Lectures use RevealJS format with custom CSS classes (`.flow`, `.highlight`, `.question`, `.incremental`)
- Tutorials include executable Python code cells
- The `execute: freeze: true` setting caches code execution results
- Output formats: HTML (primary), Hugo-MD, and Typst (PDF)
