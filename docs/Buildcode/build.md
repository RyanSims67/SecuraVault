[Back to Main Doc](../../README.md)

# Build Management

The build task was completed on the [`feature/build`](https://github.com/RyanSims67/SecuraVault/tree/feature/build) branch.

[Build File](../../securavault/build.ps1)

## Build System

Python's `setuptools` through `pyproject.toml` was used to make this build system.

The build process runs:

1. automated tests
2. Pylint
3. package creation

## Build Command

The build script calls:

```powershell
python -m pytest -v
python -m pylint src --exit-zero
python -m build
```

## First Problem

![fail1](screenshot/build-fail1.png?raw=true)

Solved by adding `build.ps1` and  editing `pyproject.toml` directly to the securavault directory.


## Second problem

![fail2](screenshot/build-fail2.png?raw=true)

Fixed by deleting the Get-Content line (and the associated output line)


## Results

After fixing the build configuration, the script ran the automated tests,
ran Pylint and created the Python package successfully.

The generated wheel and source-distribution files were placed in the
`securavault/dist` folder.

![work](screenshot/build-working.png?raw=true)

![work2](screenshot/build-working2.png?raw=true)

![work3](screenshot/build-working3.png?raw=true)

![generated files](screenshot/build-generated-files.png?raw=true)