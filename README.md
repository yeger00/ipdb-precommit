# ipdb-precommit

A pre-commit hook that automatically removes `ipdb` statements from Python files before committing.

## Features

- Removes `import ipdb` statements
- Removes `from ipdb import ...` statements
- Removes `ipdb.set_trace()` and `ipdb.breakpoint()` calls
- Works with pre-commit framework

## Installation

1. Install the package:
```bash
pip install git+https://github.com/yeger00/ipdb-precommit.git
```

2. Add the hook to your `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: local
    hooks:
    -   id: remove-ipdb
        name: Remove ipdb statements
        entry: remove-ipdb
        language: python
        types: [python]
        pass_filenames: true
```

3. Install the pre-commit hooks:
```bash
pre-commit install
```

## Usage

The hook will automatically run before each commit and remove any `ipdb` statements from your Python files. If any statements are removed, the commit will fail, and you'll see a list of the removed statements. You can then review the changes and commit again.

## Development

To set up the development environment:

1. Clone the repository:
```bash
git clone https://github.com/yeger00/ipdb-precommit.git
cd ipdb-precommit
```

2. Install development dependencies:
```bash
pip install -e .
```

## License

MIT License 