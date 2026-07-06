[Back to Main Doc](../../README.md)

# Analysis

NOTE: Based on the old version of the task.

Disclaimer: AI was used during parts of this task.

SecuraVault is a password manager project. This analysis describes the project idea, goals, users, risks, feasibility, process, stakeholders, and first system concepts before the design and implementation phase.

The analysis follows selected points, especially vision, initial situation, market analysis, feasibility, risk analysis, quality assurance, technical prototype, process model, stakeholders, use cases, business/domain classes, and system interfaces.


## Analysis Checklist Used

1. Vision and system idea
2. Initial situation and project goals
3. Target users and stakeholders
4. Market and comparable products
5. Scope and boundaries
6. Feasibility
7. Risk analysis
8. Quality assurance concept
9. Technical prototype / spike
10. Process model and deadline
11. Main use cases
12. Business/domain classes and system interfaces


## 1. Vision and System Idea

SecuraVault is a small local password manager that allows users to create, view, edit, delete, search, and generate password entries. The system should also encrypt password values before they are stored.

The vision is not to build a full replacement for professional password managers such as Bitwarden, or 1Password. Instead, the goal is to build a realistic but manageable software engineering project that demonstrates requirements engineering, Git, UML, DDD, clean code, testing, CI/CD, metrics, refactoring, and documentation.

[Prompt used: “Help me create a short vision for my password manager project that is realistic and not big.”]


## 2. Initial Situation and Project Goals

Many people reuse weak passwords or store example credentials in unsafe places during development and testing. For this project, SecuraVault focuses on managing example password entries in a structured local vault.

The starting point is intentionally simple. There is no existing system to replace. The project begins with requirements, a GitHub repository, a GitHub Projects requirements board, and Markdown documentation.

The main project goal is to build a small working prototype by the final deadline. The prototype should show that password entries can be managed and that important password-manager-specific features, such as encryption and password generation, are separated into clear modules.

The second goal is educational: to understand how software can be built using components such as Git, requirements, analysis, UML, DDD, clean code, refactoring, testing, metrics, build management, CI/CD, functional programming, and AI-assisted development.


## 3. Target Users and Stakeholders

The main target user is a person who wants to manage example password entries locally. In the context of this project, the main evaluator is also the course supervisor, who needs to see clear evidence that the software engineering tasks were applied.

Secondary users are future developers of the project. The code should be understandable enough that another developer could change password generator settings, encryption settings, or validation rules without rewriting the whole project.

| Stakeholder | Interest |
|---|---|
| Student developer | Wants a manageable project that satisfies the assignment. |
| Course supervisor | Wants evidence of software engineering concepts applied in practice. |
| Example end user | Wants to manage local password entries simply. |
| Future developer | Wants clear structure, tests, and documentation to modify the project. |

The most important stakeholder for the assignment is the course supervisor. Therefore, the README and documentation must clearly link to all evidence.

---

## 4. Market and Comparable Products

There are already many professional password managers, such as Bitwarden, 1Password, and other browser-based password managers. These products are much more advanced than SecuraVault and include features such as cloud sync, browser extensions, mobile apps, team sharing, and multi-factor authentication.

SecuraVault is different because it is not intended as a production security product. It is a learning project. The value is not market competition, but the ability to demonstrate software engineering methods using a realistic domain.

[Prompt used: “Compare this password manager with professional password managers without making unrealistic claims.”]

---

## 5. Scope and Boundaries

The project scope includes creating, viewing, editing, deleting, searching, generating, and encrypting password entries. It also includes automated tests and basic quality checks.

The project does not include browser extensions, cloud sync, mobile apps, enterprise password sharing, biometric login, or real production password storage.

| In Scope | Out of Scope |
|---|---|
| Create password entries | Browser extension |
| View password entries | Cloud sync |
| Edit password entries | Mobile app |
| Delete password entries | Enterprise password sharing |
| Search password entries | Biometric login |
| Generate passwords | Production-grade password storage |
| Encrypt stored passwords | Multi-user enterprise management |

---

## 6. Feasibility

The project is technically feasible because the planned implementation is small and uses Python. Python supports quick development, simple file/module structures, testing with pytest, and quality tools such as Ruff, Pylint, and Coverage.py.

The project is also feasible in terms of time because the first version only needs a local prototype. The main risk is not technical difficulty, but scope creep. Therefore, the implementation should stay focused on the planned requirements.

| Area | Feasibility Assessment |
|---|---|
| Technical feasibility | Feasible with Python and simple local modules. |
| Time feasibility | Feasible if the scope stays limited. |
| Documentation feasibility | Feasible using Markdown and GitHub links. |
| Testing feasibility | Feasible using pytest for core logic. |
| CI/CD feasibility | Feasible using GitHub Actions. |

---

## 7. Risk Analysis

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Scope becomes too large | High | Medium | Keep project local and avoid browser/cloud/mobile features. |
| Encryption becomes too complex | High | Medium | Use a simple library/service abstraction and document limits. |
| Documentation becomes too generic | High | Medium | Add personal notes, screenshots, and links to real files. |
| Tests are added too late | Medium | Medium | Add tests after each core module is created. |
| Git evidence is incomplete | Medium | Low | Take screenshots during branch, merge, commit, and time-travel work. |

The biggest risk is scope creep. To reduce this risk, SecuraVault will stay focused on a small local prototype instead of creating more advanced password manager features.

---

## 8. Quality Assurance Concept

Quality will be checked through automated tests, code quality tools, and manual validation checklists. The most important test areas are password generation, encryption/decryption, vault entry validation, and vault service behavior.

Quality will also be supported by clean code rules. The project should use clear file names, small functions, separated responsibilities, and limited duplication. For example, encryption logic should not be mixed directly into vault entry handling.

| Quality Area | Planned Approach |
|---|---|
| Unit testing | Use pytest for password generation, encryption, validation, and vault service logic. |
| Code style | Use Ruff or Pylint to identify style and quality problems. |
| Test coverage | Use Coverage.py to measure test coverage. |
| Manual validation | Use specification/validation checklists for the first iterations. |
| CI/CD | Run tests automatically with GitHub Actions. |

---

## 9. Technical Prototype / Spike

A small technical spike should be created before the final implementation becomes too large. The spike should prove that a password entry can be created, validated, and stored in memory or a simple local format.

A second spike can prove that encryption and decryption work correctly. This gives early feedback before the encryption service is connected to the vault service.

| Spike | Purpose |
|---|---|
| Vault entry spike | Prove that a password entry can be created and validated. |
| Encryption spike | Prove that encryption and decryption work correctly. |
| Password generator spike | Prove that random passwords can be generated with configurable settings. |

[Prompt used: “Give me a useful technical spike for a Python password manager?”]

---

## 10. Process Model and Deadline

The project will follow a small iterative process. This fits the deadline better than trying to fully plan everything before coding.

The planned iterations are:

| Iteration | Focus |
|---|---|
| Iteration 1 | Basic vault entries: create, view, edit, delete |
| Iteration 2 | Password generation, encryption, and search |
| Iteration 3 | Tests, CI/CD, metrics, clean code, and refactoring documentation |

Each iteration should produce code, documentation, and evidence such as screenshots or commit links.

The project must be completed by the final submission deadline, so the scope has to stay small. The project will be tracked through GitHub commits, GitHub Projects, Markdown documentation, screenshots, and test results.

The main project management decision is to prioritize assignment evidence over product size. A small working prototype with clear documentation is more realistic than an unfinished large application.

---

## 11. Main Use Cases

The main use cases are:

| Use Case | Description |
|---|---|
| Create password entry | User adds a new password entry to the vault. |
| View password entries | User views saved entries. |
| Edit password entry | User updates an existing entry. |
| Delete password entry | User removes an entry. |
| Generate password | User creates a strong random password. |
| Search entries | User searches entries by title, username, or URL. |
| Encrypt password | System encrypts password before storage. |

These use cases will later support the UML task, especially the use case diagram and activity diagram.

---

## 12. Business / Domain Classes and System Interfaces

The first important domain classes or modules are:

| Class / Module | Purpose |
|---|---|
| `vault_entry.py` | Represents a password entry. |
| `vault_service.py` | Handles creating, viewing, editing, deleting, and searching entries. |
| `password_generator.py` | Generates strong passwords. |
| `encryption_service.py` | Encrypts and decrypts password values. |
| `validation.py` | Checks required fields and settings. |
| `main.py` | Provides a small runnable example or CLI entry point. |

These classes are simple enough for the first implementation but still provide enough structure for UML, clean code, testing, and refactoring.

The first version of SecuraVault will use a simple local Python structure. A small command-line interface or demo script can be used to show the main features.

A future GUI is possible, but it is not required for the first version. If a GUI is added later, it should stay simple: a list of entries, a form for creating/editing entries, a search field, and a button for generating passwords.

| Interface | Description |
|---|---|
| Command-line/demo interface | Allows the main features to be demonstrated locally. |
| File/module interface | Python modules communicate through clear function and class calls. |
| Possible future GUI | Could provide forms and buttons for managing entries. |

---

## Conclusion

SecuraVault is a suitable project because it helps demonstrate the software engineering topics from the assignment. The password manager domain naturally supports requirements, analysis, UML, DDD, clean code, refactoring, testing, metrics, build management, CI/CD, and AI-assisted development.

The most important project decision is to keep the scope limited. The project should focus on a clear local prototype, strong documentation, screenshots, and personal evidence of the development process.