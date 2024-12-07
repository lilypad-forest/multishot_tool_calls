# Blog Post Tutorial Repository

This repository contains Jupyter notebooks to accompany the blog post [Your Blog Post Title].


## Colab
This project is available on colab - no local setup required.
To access the colab notebooks, visit the [colab badges](https://colab.research.google.com/github/jxnl/emp-agents/blob/main/notebooks/emp_agents_colab.ipynb)

## Setup

1. Clone this repository
2. Create a virtual env: `python -m venv venv` (Python 3.8-3.12)
3. Install the dependencies: `pip install -r requirements.txt`
4. Launch Jupyter: `jupyter notebook`


## Development
1. `nbqa mypy .` to run mypy on all the notebooks
2. `flake .` to format all source modules and notebooks.