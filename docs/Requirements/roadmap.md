[Back to Requirements Doc](requirements.md)

# Roadmap

This roadmap describes the planned development iterations for SecuraVault.

## Iteration 1 — Basic Vault Features

The first iteration focuses on the basic functionality.

### Planned Work

- Create the basic Python project structure.
- Create a password entry model.
- Add create password entry functionality.
- Add view password entries functionality.
- Add edit password entry functionality.
- Add delete password entry functionality.

### Related Requirements

- F1 — Users must be able to create password entries.
- F2 — Users must be able to view saved password entries.
- F3 — Users must be able to edit existing password entries.
- F4 — Users must be able to delete password entries.

---

## Iteration 2 — Security and Usability

The second iteration adds specific features.

### Planned Work

- Add password encryption.
- Add password generation.
- Add search functionality.
- Keep encryption logic separate from vault logic.

### Related Requirements

- F5 — Users must be able to generate strong random passwords.
- F6 — Users must be able to search password entries.
- S1 — Passwords must be encrypted before they are stored.
- Q1 — Developers must be able to easily change password generator settings.
- Q2 — Developers must be able to modify encryption settings without changing vault logic.

---

## Iteration 3 — Testing and Automation

The third iteration focuses on verification and project quality.

### Planned Work

- Add automated tests.
- Add code quality checks.

### Related Requirements

- Q3 — Developers must be able to run automated tests for the core password manager logic.