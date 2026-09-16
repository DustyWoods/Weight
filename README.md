# Weight

A lightweight command-line tool for tracking daily weight.

Weight stores records locally in SQLite and provides a simple interface for recording, viewing, and managing weight data.

## Features

- Add or update daily weight records
- Record weight for a specific date
- View recent weight records
- Display weight statistics
- Display a terminal line graph
- Customize the number of recent days
- Customize graph display
- Clear stored records
- Run from any working directory
- Lightweight and easy to install

## Installation

### Recommended: Install from GitHub Releases

Download the latest `.whl` file from [GitHub Releases](https://github.com/DustyWoods/weight/releases).

Install it with:

```bash
pipx install weight-1.0.0-py3-none-any.whl
```

Alternatively:

```bash
python -m pip install weight-1.0.0-py3-none-any.whl
```

## Usage

### Add weight

Add today's weight:

```bash
weight add 65.5
```

Add or update weight for a specific date:

```bash
weight add 65.5 --date 2026-09-16
```

### Show weight

Show recent weight records:

```bash
weight show
```

Show records from the last 7 days:

```bash
weight show --recent 7
```

Hide connecting lines in the graph:

```bash
weight show --no-lines
```

Hide statistical data:

```bash
weight show --no-data
```

Hide the graph:

```bash
weight show --no-graph
```

### Clean records

Clear all stored weight records:

```bash
weight clean
```

Skip the confirmation prompt:

```bash
weight clean --force
```

## Data Storage

Weight stores data in a platform-specific user data directory using
[platformdirs](https://github.com/tox-dev/platformdirs).

The database location follows the conventions of the operating system,
so Weight can be used across Linux, macOS, and Windows.## Development

## Development

Clone the repository:

```bash
git clone https://github.com/DustyWoods/weight.git
cd weight
```

Install the development dependencies and run the project according to the development setup.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
