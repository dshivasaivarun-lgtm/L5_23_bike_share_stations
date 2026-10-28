# Lab 5: Static Code Analysis — Bike-Share Station Manager

**Assigned repository:** [SETAPESU26/L5_23_bike_share_stations](https://github.com/SETAPESU26/L5_23_bike_share_stations)  
**Student fork:** [dshivasaivarun-lgtm/L5_23_bike_share_stations](https://github.com/dshivasaivarun-lgtm/L5_23_bike_share_stations)  
**Main file:** `bike_share_stations.py`

## 1. Project Overview

This project demonstrates static code analysis and code improvement using Pylint, Bandit, and Flake8.

The program simulates a small bike-share station manager. It supports:

- Registering bike-share stations.
- Renting bikes from stations with available inventory.
- Generating four-digit unlock PINs.
- Finding stations where the bike count equals capacity.
- Checking whether a station has bikes available.
- Resetting a station's bike inventory.

The original program contained several code-quality, security, correctness, and formatting issues. These were documented, corrected, and verified by rerunning the static analysis tools.

## 2. Software Requirements

- Python 3.10 or newer; this project was tested with Python 3.14.0.
- Git.
- Pylint.
- Bandit.
- Flake8.

## 3. Setup on Windows PowerShell

Clone the repository:

```powershell
git clone https://github.com/dshivasaivarun-lgtm/L5_23_bike_share_stations.git
cd L5_23_bike_share_stations
```

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the static analysis tools:

```powershell
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8
```

Verify the installations:

```powershell
python -m pylint --version
python -m bandit --version
python -m flake8 --version
```

## 4. Run the Program

Execute the Python script:

```powershell
python .\bike_share_stations.py
```

The program prints the results of its demonstration, including bike-rental outcomes, a generated PIN, the full stations, and bike availability.

The PIN is randomly generated and can differ between executions.

## 5. Run Static Analysis

Run each tool against the Python file and save the original reports before making changes.

### Pylint

```powershell
python -m pylint .\bike_share_stations.py > pylint_before.txt 2>&1
```

### Bandit

```powershell
python -m bandit .\bike_share_stations.py > bandit_before.txt 2>&1
```

### Flake8

```powershell
python -m flake8 .\bike_share_stations.py > flake8_before.txt 2>&1
```

After applying fixes, generate the final reports:

```powershell
python -m pylint .\bike_share_stations.py > pylint_after.txt 2>&1
python -m bandit .\bike_share_stations.py > bandit_after.txt 2>&1
python -m flake8 .\bike_share_stations.py > flake8_after.txt 2>&1
```

An empty `flake8_after.txt` indicates that Flake8 reported no violations.

## 6. Issues Identified and Fixed

The original static analysis reports identified the following problems:

- Potential SQL injection caused by string-based SQL construction.
- Inappropriate use of the `random` module for security-sensitive PIN generation.
- Broad exception handling that silently ignored errors.
- A mutable default list argument.
- Inconsistent return behavior in the bike-rental function.
- Missing checks for database query results.
- An unused variable.
- Nonstandard function naming and missing docstrings.
- Long lines, trailing whitespace, and incorrect comparisons with `None`.

The fixes included parameterized SQL queries, the `secrets` module, safer list initialization, improved error handling, consistent return values, better documentation, and formatting corrections.

See [`issues.md`](issues.md) for the detailed issue table and [`reflection.md`](reflection.md) for the lab reflection.

## 7. Analysis Results

| Tool | Original Result | Final Result |
|---|---|---|
| Pylint | 3.89/10 | 10.00/10 |
| Bandit | 3 findings: 1 medium and 2 low | No issues identified |
| Flake8 | 10 reported violations | No violations reported |

These results were obtained by running the tools against the original and updated versions of `bike_share_stations.py`.

## 8. Deliverables

The project contains the following submission files:

| File | Purpose |
|---|---|
| `bike_share_stations.py` | Updated Python source code |
| `issues.md` | Issue table documenting findings and fixes |
| `reflection.md` | Reflection on static analysis and code improvements |
| `pylint_before.txt` | Original Pylint report |
| `pylint_after.txt` | Final Pylint report |
| `bandit_before.txt` | Original Bandit report |
| `bandit_after.txt` | Final Bandit report |
| `flake8_before.txt` | Original Flake8 report |
| `flake8_after.txt` | Final Flake8 report |

## 9. Git History

The lab changes were recorded in three commits:

1. `6085165` — Improve Python code quality and fix bugs
2. `7e4ca3c` — Document security findings and remediation
3. `9c424e0` — Add analysis reports and lab reflection

The commits were pushed to the student's personal GitHub fork.

## 10. Conclusion

This lab demonstrates how static code analysis can improve the quality, security, and maintainability of Python software. Pylint, Bandit, and Flake8 provide complementary checks that help developers identify problems and verify that corrective changes have been applied.
