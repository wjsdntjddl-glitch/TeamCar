[![CodeQL Analysis](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/codeql.yml/badge.svg)](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/codeql.yml)
[![Dependency Review](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/dependency-review.yml)

# TeamCar

Apartment resident vehicle management system based on Python.

### Requirements
- [Python](https://www.python.org) >= 3.12.0
- [pytest](https://github.com/pytest-dev/pytest) >= 9.1.1

### Environment Setup
- Terminal
```
cd "PATH_TO_REPO\"
python -m venv .venv
```
Then restart the terminal to ensure working on virutal setup.

Follow the next step to upgrade pip and installing dependencies.
```
python -m pip install --upgrade pip
pip install -e .
```