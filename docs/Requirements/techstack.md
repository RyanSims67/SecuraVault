[Back to Requirements Doc](requirements.md)

# Techstack

This document describes the planned technology for SecuraVault.

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
securavault/
    config/ 
        __init__.py 
        settings.py
    
    data/

    src/
        __init__.py

        models/ 
            __init__.py 
            password_entry.py 

        services/ 
            __init__.py 
            vault_service.py 
            password_generator.py 
            encryption_service.py 
            validation.py 
            
        storage/ 
            __init__.py 
            file_storage.py 
        
        ui/ 
            __init__.py 
            cli.py

    tests/
        test_password_generator.py
        test_encryption_service.py
        test_vault_service.py
        test_file_storage.py

    README.md 
    requirements.txt 
    pyproject.toml



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