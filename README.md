# Weight

A lightweight command-line tool for tracking daily weight.

Weight stores records locally in SQLite and provides a simple interface for recording and viewing weight data.

## Features

- Add today's weight
- Update today's existing record
- Store data in a local SQLite database
- View recorded weight data
- Run from any working directory
- Lightweight and easy to install

## Installation

### Recommended: Install from GitHub Releases

Download the latest `.whl` file from the [Releases](https://github.com/DustyWoods/Weight/releases) page.

Install it with `pipx`:

```bash
pipx install weight-0.1.0-py3-none-any.whl
```

After installation, the `weight` command will be available in your terminal.

If `pipx` is not installed, see the [official installation guide](https://pipx.pypa.io/stable/installation/).

### Install a Release Directly

You can also install a specific release directly from GitHub:

```bash
pipx install https://github.com/DustyWoods/Weight/releases/download/v0.1.0/weight-0.1.0-py3-none-any.whl
```

### Upgrade

Download the newer wheel from the Releases page and install it:

```bash
pipx install --force weight-0.2.0-py3-none-any.whl
```

### Uninstall

```bash
pipx uninstall weight
```

## Usage

### Add Today's Weight

```bash
weight add 68.5
```

If a record already exists for today, it will be updated.

### Show Weight Records

```bash
weight show
```

### Get Help

```bash
weight --help
weight add --help
weight show --help
```

## Data Storage

Weight uses SQLite to store weight records locally.

The database is stored in a user-specific data directory rather than in the directory from which the command is executed.

This allows Weight to be used from any working directory while keeping data separate from the project source code.

## Development

Clone the repository:

```bash
git clone https://github.com/DustyWoods/Weight.git
cd weight
```

Install the project in editable mode:

```bash
pip install -e .
```

Install development dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
python -m unittest discover
```

## Project Structure

```text
Weight/
├──  pyproject.toml             # Project metadata and build configuration
├──  README.md
├──  requirements.txt           # Development dependencies
├──  src
│   └──  weight
│       ├──  __init__.py
│       ├──  __main__.py        # Application entry point
│       ├──  config.py          # Configuration and path management
│       ├──  database.py        # Database operations
│       ├──  handler.py         # Command handling
│       ├──  models.py          # Data models
│       ├──  parser.py          # Command-line argument parsing
│       ├──  repository.py      # Data access layer
│       ├──  utils.py           # Data rendering and visualization
│       └──  validators.py      # Data validators
└──  tests/                     # Unit tests
```

## Requirements

- Python 3.14
- SQLite

## License

This project is licensed under the MIT License.
