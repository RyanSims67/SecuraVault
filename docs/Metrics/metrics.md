[Back to Main Doc](../../README.md)

# Metrics

Test coverage and Pylint were used to measure this project.

## Metric 1 — Test Coverage

Command ran:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

My result was: 36% total coverage


The coverage table showed which files were executed by the automated tests and which lines were missed.

The file with the lowest coverage was: src\ui\cli.py and src\ui\gui.py with 0%

These files had lower coverage because they depend on direct user interaction.

The CLI waits for keyboard input, while the GUI depends on buttons, input fields and window events. 

My current unit tests focus on the main program logic, such as the vault service, encryption, password generation and file storage.

I could further test the CLI and GUI in the future, such as mocking user input or using GUI testing tools.



![Coverage result](screenshots/metrics-coverage.png?raw=true)

## Metric 2 — Pylint

I ran:

```bash
python -m pylint src
```

My Pylint score was: 6.52/10

The main warnings I noticed were:

- `missing-function-docstring`
- `missing-final-newline`
- `import-error`

One warning I understood was:

```text
missing-function-docstring
```
where a function does not contain a short explanation of its purpose.

![Pylint result](screenshots/metrics-pylint1.png?raw=true)
![Pylint result](screenshots/metrics-pylint1.png?raw=true)
![Pylint result](screenshots/metrics-pylint1.png?raw=true)
![Pylint result](screenshots/metrics-pylint1.png?raw=true)


## What the Metrics Showed Me

Test coverage showed me which parts of SecuraVault were reached by the automated tests.

Pylint showed me that code can still run correctly while containing style, naming or documentation problems.

The metrics helped me find areas that could be improved instead of relying only on whether the application opened successfully.

## Result

Both metrics were executed successfully and documented with screenshots.

The results gave me measurable information about testing and code quality.