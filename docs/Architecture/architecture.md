[Back to Main Doc](../../README.md)

# Architecture

For this task, I created an Architecture Communication Canvas for SecuraVault.

The link to the Architecture Communication Canvas can be found at [Miro Board](https://miro.com/app/board/uXjVHGTr37E=/?share_link_id=775805985493)

## Architecture Communication Canvas

![SecuraVault Architecture Communication Canvas](screenshots/architecture-communication-canvas.jpg?raw=true)

## Value Proposition

SecuraVault is a simple local password manager.

It allows users to:

- store password entries locally
- generate random passwords
- search and update saved entries
- use either a command line interface or graphical interface
- store passwords in encrypted form instead of plain text

The system was created as a project and is not intended to replace a production password manager.

## Key Stakeholders

The main stakeholders are:

| Stakeholder           | Interest                                                     |
| --------------------- | ------------------------------------------------------------ |
| End user              | Wants to manage saved passwords using a simple interface     |
| Developer             | Maintains, updates and tests the application                 |
| Lecturer or evaluator | Reviews the assignment and the software-engineering evidence |
| Future contributor    | May extend the project with additional features              |

The most important stakeholder is the end user because the application exists to help them manage password entries.

## Core Functions

The main functions of SecuraVault are:

1. create password entries
2. view saved entries
3. edit entries
4. delete entries
5. search by title or username
6. generate random passwords
7. encrypt passwords before storage
8. save entries to a local JSON file
9. load entries when the application starts
10. provide both CLI and GUI access

These functions represent the current scope of the project.

## Quality Requirements

The main quality requirements are:

### Security

Passwords must be encrypted before they are written to the JSON file.

### Usability

The system should be simple to use through both the CLI and GUI.

### Maintainability

The code should be separated into clear modules so that changes are easier to locate.

### Changeability

Features such as storage, encryption and password generation should be changeable without rewriting the complete application.

### Testability

The core services should be testable without opening the GUI or changing real user data.

### Reliability

Invalid input and missing entry IDs should produce understandable error messages.

### Deployability

The application should be testable and buildable through the local build script and GitHub Actions.

### Readability

Functions and files should use names that explain their purpose.

## Business Context

SecuraVault runs as a local application.

The user interacts with the system through either the CLI or GUI.

![business](screenshots/business-context.png?raw=true)

The main external elements are:

| External element     | Relationship                                  |
| -------------------- | --------------------------------------------- |
| User                 | Creates and manages password entries          |
| Operating system     | Runs Python and provides local file storage   |
| Local file system    | Stores the encrypted vault and encryption key |
| Cryptography library | Provides Fernet encryption                    |
| GitHub               | Stores the code, branches and documentation   |
| GitHub Actions       | Runs tests, Pylint and the package build      |


## Components and Modules

The current source-code structure is:

```text
securavault/
├── config/
├── src/
│   ├── models/
│   ├── services/
│   ├── storage/
│   └── ui/
└── tests/
```

The main components are:

| Component           | Responsibility                                           |
| ------------------- | -------------------------------------------------------- |
| `PasswordEntry`     | Represents one saved password entry                      |
| `VaultService`      | Handles create, view, edit, delete and search operations |
| `Validation`        | Checks required fields                                   |
| `PasswordGenerator` | Creates random passwords                                 |
| `EncryptionService` | Encrypts and decrypts passwords                          |
| `FileStorage`       | Saves and loads entries from JSON                        |
| CLI                 | Provides terminal interaction                            |
| GUI                 | Provides window-based interaction                        |
| Settings            | Stores paths and default values                          |
| Tests               | Verify the main services and storage behaviour           |

## Component Interaction


![component](screenshots/component-interation.png?raw=true)


The CLI and GUI both use `VaultService`.

This means the application does not contain separate copies of the vault logic for each interface.

## Core Architecture Decisions

### Shared Service Layer

Both the CLI and GUI use `VaultService`.

This prevented duplicated create, edit, delete and search logic.

### Local JSON Storage

I used JSON because it was simple to implement and inspect during development.

The disadvantage is that it is not suitable for large or multi-user systems.

### Fernet Encryption

I used the `cryptography` library instead of creating my own encryption algorithm.

This reduced the risk of implementing unsafe custom encryption.

### Separate Modules

Models, services, storage and user interfaces are stored separately.

This created more files, but made the project easier to understand and test.

### Dependency Injection for Testing

`VaultService` can receive another storage object, and `FileStorage` can receive another encryption service.

This allowed the tests to use temporary files, fake storage and mocks.

### Central Configuration

File paths and the default password length are stored in `settings.py`.

This made the values easier to change.

### Automated Testing and Building

pytest, Pylint and package building are run locally and through GitHub Actions.

This helps identify problems before changes are merged.

## Technologies

The technologies used are:

| Technology       | Purpose                      |
| ---------------- | ---------------------------- |
| Python           | Main programming language    |
| Tkinter          | Graphical user interface     |
| JSON             | Local vault-file format      |
| `pathlib`        | File-path handling           |
| `cryptography`   | Fernet encryption            |
| pytest           | Automated testing            |
| pytest-cov       | Test coverage                |
| `unittest.mock`  | Mock testing                 |
| Pylint           | Code-quality analysis        |
| setuptools       | Package build                |
| `pyproject.toml` | Build configuration          |
| PowerShell       | Local build script           |
| Git              | Version control              |
| GitHub           | Repository hosting           |
| GitHub Actions   | Continuous delivery pipeline |

## Risks and Missing Information

The canvas helped me identify the following risks:

| Risk                            | Possible effect                                    | Future improvement                          |
| ------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| No master password              | Anyone using the computer may open the vault       | Add master-password authentication          |
| Key stored locally              | Access to both files may allow decryption          | Use operating-system key storage            |
| Passwords shown in plain text   | Someone looking at the screen may see them         | Hide passwords and add a reveal button      |
| No damaged JSON handling        | A corrupted file may stop the vault loading        | Catch JSON errors and add recovery          |
| No backup feature               | Deleted or lost files cannot be recovered          | Add encrypted export and backup             |
| No automatic GUI tests          | Some interface problems may only be found manually | Add GUI testing later                       |
| No cloud synchronisation        | Entries are only available on one device           | Add secure synchronisation only if required |
| No professional security review | Security weaknesses may remain                     | Perform a security review before real use   |
| Lost encryption key             | Existing vault data becomes unreadable             | Add a documented recovery process           |


## Review Against Architecture Principles

| #  | Principle              | SecuraVault result                                         |
| -- | ---------------------- | ---------------------------------------------------------- |
| 1  | Modularity             | Models, services, storage and UI are separated             |
| 2  | Cohesion               | Each module contains closely related responsibilities      |
| 3  | Loose coupling         | UI code depends on `VaultService`, not directly on storage |
| 4  | Separation of concerns | Validation, encryption and storage are separate            |
| 5  | Abstraction            | Services hide implementation details from the UI           |
| 6  | Information hiding     | Storage and encryption details are not handled by the GUI  |
| 7  | Changeability          | Settings and dependencies can be changed separately        |
| 8  | Maintainability        | Responsibilities are divided across small files            |
| 9  | Readability            | Functions use descriptive names                            |
| 10 | Testability            | Services can be tested without opening the application     |
| 11 | Reliability            | Validation and exception tests check invalid input         |
| 12 | Security               | Passwords are encrypted before storage                     |
| 13 | Deployability          | A repeatable package build exists                          |
| 14 | Continuous delivery    | GitHub Actions automatically runs tests and the build      |
| 15 | Self-documentation     | The repository includes diagrams and supporting documents  |

## Personal Experience

At the beginning of the project, SecuraVault only needed a small command line interface and an in memory list.

As I added file storage, encryption, password generation, tests and a GUI, keeping everything inside one file would have become difficult to manage.

The separation between `VaultService`, `FileStorage` and `EncryptionService` helped me structure the files easier and more cleaner.

For example, the storage tests could use a temporary encryption key instead of using the real key from the application.

Creating the canvas also made me notice weaknesses that were not obvious when I only checked whether the program worked.

The main weakness is that the application stores the encryption key locally and does not require a master password to access this password manager.

