[![CodeQL Analysis](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/codeql.yml/badge.svg)](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/codeql.yml)
[![Dependency Review](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/wjsdntjddl-glitch/TeamCar/actions/workflows/dependency-review.yml)

# TeamCar

Apartment resident vehicle management system based on Python.

### Requirements
- [Python](https://www.python.org) >= 3.12.0
- [pytest](https://github.com/pytest-dev/pytest) >= 9.1.1
- [wcwidth](https://github.com/jquast/wcwidth) >= 0.9.4

### Environment Setup
Follow the next step to launch venv + upgrade pip and installing dependencies.
- Terminal
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .

```

### Build
- Terminal
```
build.bat
```