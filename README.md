
# GitHub User Activity CLI

A simple Python command-line application that fetches and displays a GitHub user's recent public activity.

Built as part of the [roadmap.sh GitHub User Activity project](https://roadmap.sh/projects/github-user-activity).

## Features

- Fetch recent public activity using the GitHub REST API.
- Display GitHub events in a human-readable format.
- Handle invalid usernames and common API errors.
- Run directly from the command line.
- Use Python's standard library for API requests.

## Requirements

- Python 3.12 or newer
- Internet connection

## Installation

Clone the repository:

```bash
git clone <https://github.com/masoud-vosoughi/github-user-activity.git>
cd github-user-activity
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the application:

```bash
python -m pip install -e .
```

## Usage

Fetch a user's activity:

```bash
github-activity torvalds
```

Example output:

```text
- Pushed to torvalds/linux
- Pushed to torvalds/linux
- Activity in torvalds/linux
```

Display help:

```bash
github-activity --help
```

## Testing

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
python -m pytest -v
```

Check code quality:

```bash
python -m ruff check .
python -m ruff format --check .
```

## Project Structure

```text
src/github_activity/
├── cli.py
├── client.py
└── formatter.py

tests/
└── test_cli.py
```

## Limitations

- Only recent public GitHub events are retrieved.
- Some event types use a generic description.
- The application currently fetches only the first page of events.
- GitHub API rate limits apply.
