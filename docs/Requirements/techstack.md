[Back to Requirements Doc](requirements.md)

# Techstack

This document describes the planned technology for SecureVault.

#### Programming Language - Python

#### Documentation - Markdown


## Tools

| Area | Tool |
|---|---|
| Version Control | Git and GitHub |
| Requirements Tool | GitHub Projects |
| Documentation | Markdown |
| Testing | pytest |
| Code Quality | Ruff or Pylint |
| Metrics | Coverage.py |
| CI/CD | GitHub Actions |

## Planned Project Structure

```text
src/
    __init__.py
    vault_entry.py
    vault_service.py
    password_generator.py
    encryption_service.py
    validation.py
    main.py

tests/
    test_password_generator.py
    test_encryption_service.py
    test_vault_service.py

docs/
    Analysis/
    Buildcode/
    Clean_code_development/
    Continous_Delivery/
    DDD/
    Git/
    Metrics/
    Refactoring/
    Requirements/
    Screenshots/
    Testing/
    UML/