# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without running the program. It helps find possible bugs, security problems and style issues early. This makes code easier to maintain and can reduce the chance of errors.

### 2. What are the differences between Pylint, Bandit and Flake8?

Pylint checks general code quality, naming, documentation and programming practices. Bandit looks for common security risks. Flake8 checks Python style and formatting, such as line length and comparisons with `None`. Using all three gives a broader review than relying on just one tool.

### 3. What issues did you find and fix in the scholarship program?

The original program had a possible SQL injection issue because it built a query using string formatting. I changed it to use SQL parameters. I also replaced the mutable default list with `None`, removed the shell command and unnecessary exception handling, and corrected naming and documentation issues. These changes made the code safer and easier to read.

### 4. How does static analysis improve code quality and maintainability?

Static analysis provides consistent feedback and helps developers notice problems they might miss during manual review. It does not prove that a program is completely correct, so the code still needs to be run and tested. In this lab, the tools helped identify specific improvements and verify the changes afterward.
