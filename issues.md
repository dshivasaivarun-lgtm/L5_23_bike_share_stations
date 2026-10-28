# Lab 5: Static Code Analysis — Issue Report

**Project:** Bike-Share Station Manager  
**File analyzed:** `bike_share_stations.py`  
**Tools:** Pylint, Bandit, Flake8

## 1. Issues identified and fixes applied

| Issue | Type | Original line(s) | Tool / Finding | Description | Fix Approach |
|---|---|---:|---|---|---|
| SQL query construction | Security | 9 | Bandit B608 | SQL was constructed through string concatenation, creating a potential SQL injection vulnerability. | Replaced concatenation with parameterized SQL placeholders. |
| Weak random-number generator | Security | 22 | Bandit B311 | The `random` module was used for security-sensitive PIN generation. | Replaced it with `secrets.randbelow()`. |
| Broad exception handling | Quality / Security | 32–35 | Bandit B110; Pylint W0718 | A broad exception was caught and silently ignored. | Removed unnecessary exception handling so unexpected errors are not hidden. |
| Mutable default argument | Bug / Quality | 8 | Pylint W0102 | The default `log=[]` list could be shared across function calls. | Changed the default to `None` and initialized a list inside the function. |
| Inconsistent return behavior | Bug / Quality | 14–19 | Pylint R1710 | The bike-rental function returned a Boolean on success but implicitly returned `None` on failure. | Made the function return `True` on success and `False` otherwise. |
| Missing query-result check | Bug | 38–41 | Code review | A missing station could produce a `None` query result that was indexed without checking. | Checked whether the result and its bike count were `None`. |
| Unused variable | Quality | 27 | Pylint W0612; Flake8 F841 | The `summary` variable was calculated but never used. | Removed the unused variable. |
| Nonstandard function names | Style | Multiple | Pylint C0103 | Function names used camelCase rather than Python's snake_case convention. | Renamed functions, such as `addStation()` to `add_station()`. |
| Missing docstrings | Documentation | Multiple | Pylint C0114, C0116 | The module and functions lacked documentation strings. | Added a module docstring and function docstrings. |
| Long lines and whitespace | Style | Multiple | Pylint C0301, C0303; Flake8 E501, W291 | Several lines exceeded style limits or contained trailing whitespace. | Reformatted SQL statements and other long lines and removed trailing whitespace. |
| Incorrect `None` comparison | Style / Quality | 40 | Pylint C0121; Flake8 E711 | The code used `== None` instead of an identity check. | Used `is None` checks. |
| Missing final newline | Style | End of file | Pylint C0304; Flake8 W292 | The original final file line did not end with a newline. | Added the required final newline. |

**Note:** The line numbers refer to the original script. Multiple findings may refer to the same underlying problem. The missing query-result check was identified by code review; it should not be represented as a confirmed original Pylint, Bandit, or Flake8 finding.

## 2. Verification results

| Tool | Original result | Final result |
|---|---|---|
| Pylint | 3.89/10 | 10.00/10 |
| Bandit | 3 findings: 1 medium, 2 low | No issues identified |
| Flake8 | 10 reported violations | No violations reported |

## 3. Conclusion

The program was updated to address the security, correctness, documentation, and formatting issues identified in the original source. All three tools were rerun against the updated script, and the final reports showed a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations.
