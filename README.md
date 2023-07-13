# GPT-Engineer Wrapper (gm-engineer)

This is a Python script to facilitate the usage of the `gpt-engineer` tool. It is designed to load environment variables from a `.env` file and then run the `gpt-engineer` tool with the provided project name. Optionally, it can include a feedback step.

## Setup

1. Make sure you have the `gpt-engineer` and `python-dotenv` packages installed:

```bash
pip3 install gpt-engineer python-dotenv
```

2. Create a `.env` file in the same directory as the `gm-engineer.py` script and set your OpenAI API key:

```text
OPENAI_API_KEY=your_openai_api_key
```

Make sure to replace `your_openai_api_key` with your actual OpenAI API key.

## Usage

You can run the `gm-engineer.py` script with your project's name as a command line argument:

```bash
python3 gm-engineer.py projects/your_project_name
```

Replace `your_project_name` with the name of your project.

To include the feedback step, you can add the `--feedback` flag:

```bash
python3 gm-engineer.py --feedback projects/your_project_name
```

## Requirements

This script requires the following:

* Python 3
* `gpt-engineer`
* `python-dotenv`

## GPT-Engineer

This script is a wrapper for the `gpt-engineer` tool. You can find more information about `gpt-engineer` in its [GitHub repository](https://github.com/AntonOsika/gpt-engineer).
