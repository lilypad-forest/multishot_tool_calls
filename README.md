# Multi-Shot Tool Call Tutorial

This repository contains notebooks and source code to accompany the blog post [Effective Multi-Shot Tool Call Prompting
](https://electronicsilk.substack.com/p/effective-multi-shot-tool-call-prompting).

## Overview
We're using the [EMP framework](https://github.com/empyrealapp/emp-agents) to take advantage of its tool and message abstractions.
We've set up a simple example of a cooking assistant with access to a set of tools defined under `src/tools`.

There are three examples:
1. zero shot
2. multi-shot with provider agnostic tool calling
3. multi-shot with provider specific tool calling.

Each example runs the inference and prints the conversation so you can inspect what the messages look like. Pay attention to the system prompt since that's where we've stuffed the examples; of course, the same tactic would work stuffing into user messages.

## Setup
1. Clone this repository
2. Create a virtual env: `python -m venv venv` (Python 3.8-3.12)
3. Install the dependencies: `pip install -r requirements.txt`
4. Add your OpenAI API key into a .env file, like `OPENAI_API_KEY=sk-...`
5. Launch Jupyter: `jupyter notebook`


## Development
1. `nbqa mypy .` to run mypy on all the notebooks
2. `flake .` to format all source modules and notebooks.