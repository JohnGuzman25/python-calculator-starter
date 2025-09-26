# Python Calculator Starter

A minimal, production‑ready Python calculator package with:

- **src/** layout
- **pytest** for tests (+ coverage)
- **pylint** for linting
- **GitHub Actions** CI (lint + tests + coverage artifact)

## Quickstart (local)

```bash
# 1) (Recommended) create & activate a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run lint + tests with coverage
pylint src tests
pytest --cov=src/calculator --cov-report=term-missing
```

## Use in Python
```python
from calculator import calc
calc.add(2, 3)        # 5
calc.subtract(5, 2)   # 3
calc.multiply(4, 6)   # 24
calc.divide(20, 5)    # 4.0
```

## CLI usage
After installing requirements, you can run:
```bash
python -m calculator add 2 3
python -m calculator div 10 2
```

## VS Code tips
- Open this folder in VS Code.
- Select your interpreter: **Command Palette → Python: Select Interpreter → .venv**.
- Install the Python extension for linting/test UI.
- Tests are auto‑discovered under `tests/` (pytest).

## Repo layout
```text
.
├── .github/workflows/ci.yml
├── .gitignore
├── .pylintrc
├── .coveragerc
├── README.md
├── requirements.txt
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── __main__.py
│       └── calc.py
└── tests/
    └── test_calc.py
```
