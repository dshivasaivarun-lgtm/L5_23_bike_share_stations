\# Lab 5: Static Code Analysis — Issues



| Issue | Type | Line(s) in original file | Description | Fix Approach |

|---|---|---|---|---|

| SQL query construction | Security | 9 | String concatenation in SQL created a potential SQL injection vulnerability. | Used parameterized SQL with placeholders. |

| Weak random PIN generation | Security | 22 | The `random` module is not suitable for security-sensitive PIN generation. | Replaced it with `secrets.randbelow()`. |

| Mutable default argument | Bug | 8 | The default list could be shared across calls. | Used `None` and initialized the list inside the function. |

| Broad exception handling | Quality | 34–35 | Catching and ignoring all exceptions could hide database errors. | Removed unnecessary broad exception handling. |

| Missing database-result check | Bug | 39–40 | Indexing a missing query result could cause an error. | Checked whether the result was `None`. |

| Unused variable | Quality | 27 | The `summary` variable was never used. | Removed the unused variable. |

| Naming and documentation | Style | Multiple | Function names did not follow snake\_case, and docstrings were missing. | Renamed functions and added docstrings. |

| Formatting violations | Style | Multiple | Long lines, trailing whitespace, and a missing final newline violated style rules. | Corrected formatting and added the final newline. |



\## Final verification



\- Pylint: 10.00/10

\- Bandit: No issues identified

\- Flake8: No violations reported

\- Program execution: Successful



