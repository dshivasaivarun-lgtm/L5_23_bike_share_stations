\# Lab 5: Static Code Analysis — Reflection



\## 1. What did you learn about static code analysis?



Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations. It helps improve software quality and maintainability.



\## 2. How did Pylint, Bandit, and Flake8 differ?



Pylint identified code-quality issues such as missing docstrings, naming problems, unused variables, and dangerous defaults. Bandit identified security concerns such as unsafe SQL construction and unsuitable random-number generation. Flake8 detected formatting and style violations.



\## 3. What issues did you fix?



I used parameterized SQL queries, replaced the standard random-number generator with the `secrets` module, removed the mutable default argument, improved exception handling, checked for missing database rows, removed unused code, and corrected naming and formatting issues.



\## 4. How did static analysis improve your code?



Static analysis helped me find and correct problems systematically. The Pylint score improved from 3.89/10 to 10.00/10. Bandit reported no remaining issues, and Flake8 reported no violations after the final newline fix.



