[Back to Main Doc](../../README.md)

# Continuous Delivery

The Continuous Delivery task can be found in the [GitHub Actions file](../../.github/workflows/ci.yml)

## Goal

The goal is to automatically test and build SecuraVault whenever code is pushed to GitHub.

## Tool Used

GitHub Actions was used for this task.

The workflow file is located at:

```text
.github/workflows/ci.yml
```

## Pipeline Steps

The pipeline performs the following steps:

1. downloads the repository
2. installs Python
3. installs the required dependencies
4. runs the automated tests
5. runs Pylint
6. builds the Python package

## Workflow Commands

The main commands used by the pipeline are:

```bash
python -m pytest -v
python -m pylint src --exit-zero
python -m build
```

## Trigger

The workflow runs when code is pushed to:

```text
main
feature/continuous-delivery
```

It also runs when a pull request is opened against `main`.


## Script Calls

![pytest](screenshot/ci-pytest.png?raw=true)

![pylint](screenshot/ci-pylint.png?raw=true)


## Successful Run

The final workflow completed successfully.

![Successful workflow](screenshot/ci-success.png?raw=true)
