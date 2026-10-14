# Static Code Analysis — Issues Report

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL query constructed using string formatting | Security — Medium | 10 | Values are inserted directly into an SQL query, creating a potential SQL injection vulnerability. | Replace string formatting with a parameterized SQL query using placeholders. |
| Mutable default argument | Bug / Code Quality | 9 | The default argument `audit=[]` creates a shared list that may retain data across function calls. | Use `None` as the default and initialize a new list inside the function. |
| Shell command execution | Security — Low | 26 | `os.system()` invokes a shell to execute a command, which is flagged by Bandit. | Replace the shell command with a direct Python operation, such as `print()`, if appropriate. |
| Exception silently ignored | Error Handling — Low | 25–28 | The broad exception handler catches any exception and ignores it using `pass`, hiding potential failures. | Remove unnecessary exception handling or catch a specific exception and handle it appropriately. |
| Use of global variable | Code Quality | 16 | The `global disbursed_total` statement creates shared mutable state and makes the function harder to test and maintain. | Refactor the function to return the updated total or manage the total through a suitable data structure. |
| Inconsistent return statements | Code Quality | 15–21 | `disburse()` returns an amount when an award exists but returns nothing when it does not. | Define consistent behavior for missing award IDs, such as explicitly returning `None`. |
| Comparison with `None` using `==` | Style | 32 | The expression `scheme == None` violates Python style conventions. | Replace it with `scheme is None`. |
| Lines exceeding recommended length | Style | 5, 10, 17, 19, 34 | Several lines exceed the line lengths reported by Pylint and Flake8. | Split long statements across multiple lines using appropriate indentation. |
| Missing docstrings | Documentation / Style | 1, 9, 15, 24, 31, 37 | The module and several functions do not have docstrings explaining their purpose. | Add a module docstring and concise docstrings to the functions. |
| Function naming convention | Style | 31 | `bySchemeCount` uses camelCase instead of the recommended snake_case convention. | Rename it to `by_scheme_count` and update its call sites. |
| Unnecessary import after refactoring | Code Quality | 1 | The `os` import will become unnecessary if shell execution is removed. | Remove imports that are no longer required after refactoring. |
