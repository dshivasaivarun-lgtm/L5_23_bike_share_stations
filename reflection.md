# Lab 5: Static Code Analysis — Reflection

# 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, coding-standard violations, and maintainability problems.

In this lab, I applied static code analysis to a Python bike-share station management program. The program supports registering stations, renting bikes, generating unlock PINs, finding full stations, checking bike availability, and resetting station inventory.

Static analysis was useful because it identified issues that might not be obvious during normal execution. For example, the program could run successfully while still containing a potential SQL injection vulnerability, an unsafe mutable default argument, and incorrect error-handling practices.

The lab demonstrated that static analysis should be an important part of the software development process. It helps developers identify defects early, improve code quality, strengthen security, and make programs easier to maintain.

# 2. What are the differences between Pylint, Bandit, and Flake8?

I used three static analysis tools, each with a different primary purpose.

### Pylint

Pylint examines Python code quality, programming practices, naming conventions, documentation, and potential logical errors.

In the original program, Pylint reported missing module and function docstrings, inconsistent function naming, a dangerous mutable default argument, inconsistent return statements, an unused variable, broad exception handling, and formatting problems.

After correcting the issues, the Pylint score improved from 3.89/10 to 10.00/10.

### Bandit

Bandit focuses on identifying common security vulnerabilities in Python programs.

The original program produced three findings:

- **B608 — Hardcoded SQL expressions:** The station name and numeric values were concatenated into an SQL statement, creating a potential SQL injection risk.
- **B311 — Standard pseudo-random generator:** The `random` module was used to generate unlock PINs even though it is unsuitable for security-sensitive randomness.
- **B110 — Try/except/pass:** A broad exception handler silently ignored errors.

I corrected the SQL query by using parameterized statements, replaced `random.randint()` with `secrets.randbelow()`, and removed the unnecessary broad exception handler.

The final Bandit scan reported no issues.

### Flake8

Flake8 checks Python style and formatting, including whitespace, line length, and certain programming errors.

The original report identified long lines, an unused variable, trailing whitespace, and an incorrect comparison with `None`.

I reformatted the code, removed the unused variable, used `is None` checks where appropriate, and added the missing final newline.

The final Flake8 report contained no violations.

# 3. What problems did you identify and how did you fix them?

I identified and corrected several issues in the bike-share station program.

### SQL injection risk

The original `addStation()` function constructed an SQL statement using string concatenation. If a station name contained SQL syntax, it could alter the intended query.

I replaced string concatenation with parameterized SQL using placeholders and a separate tuple of values. This allows SQLite to handle the supplied values as data rather than SQL syntax.

### Mutable default argument

The original function used `log=[]` as a default argument. Mutable default objects can persist between function calls and cause unintended sharing of state.

I changed the default to `None` and initialized a new list inside the function when no log is supplied.

### Insecure random-number generation

The original `unlockPin()` function used `random.randint()` to generate a four-digit PIN.

I replaced it with `secrets.randbelow(9000) + 1000`, which generates a PIN between 1000 and 9999 using a cryptographically suitable random source.

### Broad exception handling

The original `resetStation()` function caught every `Exception` and silently ignored it. This could hide unexpected failures and make debugging difficult.

I removed the unnecessary exception handler so that unexpected database errors are not silently concealed.

### Missing database-result checks

The original `hasBikes()` function accessed the first element of a query result without verifying that the station existed.

I added checks for a missing row and a `None` bike count before comparing the number of bikes.

### Code quality and formatting

I also renamed functions to follow Python's snake_case convention, added docstrings, removed the unused `summary` variable, corrected inconsistent return behavior, and fixed formatting violations.

These changes made the program more readable, maintainable, and robust while preserving its main functionality.

# 4. How did static analysis improve the program, and what did I learn?

The original program ran, but its static analysis reports revealed several security, quality, and style problems.

The results were:

| Tool | Before fixes | After fixes |
|---|---|---|
| Pylint | 3.89/10 | 10.00/10 |
| Bandit | 3 findings: 1 medium and 2 low severity | No issues identified |
| Flake8 | 10 reported violations | No violations |

The Pylint score improved by 6.11 points. Bandit and Flake8 also confirmed that the findings they reported in the original program were addressed.

Through this lab, I learned that different static analysis tools complement one another. Pylint focuses on general code quality, Bandit focuses on security, and Flake8 focuses on style and formatting.

I also learned that a successful program execution does not guarantee secure or maintainable code. Automated tools can identify problems that may be missed during manual review, but their findings still need to be understood and evaluated by the developer.

Overall, static code analysis improved the quality of my program and provided a repeatable way to verify changes. I would use these tools during development and before committing code in future projects.
