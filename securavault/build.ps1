$ErrorActionPreference = "Stop"

Write-Host "Running automated tests..."
python -m pytest -v

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed. Build stopped."
    exit $LASTEXITCODE
}

Write-Host "Running Pylint..."
python -m pylint src --exit-zero


Write-Host "Building SecuraVault package..."
python -m build

if ($LASTEXITCODE -ne 0) {
    Write-Host "Package build failed."
    exit $LASTEXITCODE
}

Write-Host "Build completed successfully."