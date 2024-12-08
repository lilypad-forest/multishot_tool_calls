# Multi-Shot Tool Call Tutorial

This repository contains notebooks and source code to accompany the blog post [Effective Multi-Shot Tool Call Prompting
](https://electronicsilk.substack.com/p/effective-multi-shot-tool-call-prompting).

## Overview
We're using the [EMP framework](https://github.com/empyrealapp/emp-agents) to take advantage of its tool and message abstractions.
We've set up a simple example of a cooking assistant with access to a set of tools defined under `src/tools`.

## Setup
1. Clone this repository
2. Create a virtual env: `python -m venv venv` (Python 3.8-3.12)
3. Install the dependencies: `pip install -r requirements.txt`
4. Launch Jupyter: `jupyter notebook`


## Development
1. `nbqa mypy .` to run mypy on all the notebooks
2. `flake .` to format all source modules and notebooks.