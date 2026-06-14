[Back to Requirements Doc](requirements.md)

# Iteration 2

## Goal

The goal of Iteration 2 is to add the main specific features for SecuraVault: password generation, password encryption, and search functionality.

## Related Requirements

- F5 — Users must be able to generate strong random passwords.
- F6 — Users must be able to search password entries.
- S1 — Passwords must be encrypted before they are stored.
- Q1 — Developers must be able to easily change password generator settings.
- Q2 — Developers must be able to modify encryption settings without changing vault logic.

## Specifications

| Feature | Required | Description |
|---|---|---|
| Password Generator | Yes | Creates strong random passwords. |
| Generator Settings | Yes | Allows password length and character options to be changed. |
| Password Encryption | Yes | Encrypts password values before storage. |
| Encryption Separation | Yes | Keeps encryption logic separate from vault logic. |
| Search | Yes | Allows users to search saved password entries. |
| Search Fields | Yes | Supports search by title, username, and URL. |

## Planned Files

| File | Purpose |
|---|---|
| `src/password_generator.py` | Handles password generation logic. |
| `src/encryption_service.py` | Handles encryption and decryption logic. |
| `src/vault_service.py` | Uses the generator/encryption services where needed. |
| `src/validation.py` | Contains validation rules for entries and settings. |
| `tests/test_password_generator.py` | Tests password generation behavior. |
| `tests/test_encryption_service.py` | Tests encryption and decryption behavior. |
| `tests/test_vault_service.py` | Tests search and vault behavior. |

## Validation Plan

Iteration 2 is valid when password generation, encryption, and search work correctly and tested.

| Validation Check | Expected Result | Status |
|---|---|---|
| Generate password | A random password is generated. | Passed |
| Password length setting | The generated password uses the configured length. | Passed |
| Password character settings | The generated password can use configured character groups. | Passed |
| Encrypt password | A plain password is converted into an encrypted value. | Passed |
| Encrypted value differs from plain text | The stored encrypted value is not the same as the original password. | Passed |
| Decrypt password | The encrypted value can be decrypted when needed. | Passed |
| Search by title | Matching entries can be found by title. | Passed |
| Search by username | Matching entries can be found by username. | Passed |
| Separation of encryption logic | Encryption code is kept separate from vault entry logic. | Passed |


## Initial Screenshots

### Menu

![Menu](iteration2_screenshots/iteration2-menu.png?raw=true)

### Create generated password

![create](iteration2_screenshots/iteration2-create-generated-password.png?raw=true)

![generator](iteration2_screenshots/iteration2-password-generator.png?raw=true)

### View Password entries

![view](iteration2_screenshots/iteration2-view-entry.png?raw=true)

### Edit password entry

![Edit](iteration2_screenshots/iteration2-edit-entry.png?raw=true)

### Delete password entry

![Delete](iteration2_screenshots/iteration2-delete-entry.png?raw=true)

### Search password entry

![search](iteration2_screenshots/iteration2-search.png?raw=true)

### Storage

![storage](iteration2_screenshots/iteration2-storage.png?raw=true)

### Required field validation

![invalid id](iteration2_screenshots/iteration2-invalid-id.png?raw=true)

![length](iteration2_screenshots/iteration2-password-length-error.png?raw=true)

### Encryption

![encryption test](iteration2_screenshots/encryption.png?raw=true)



## Graphical User Interface (GUI)

A basic Tkinter graphical interface was added during Iteration 2.

The interface allows the user to:

- enter a password manually
- generate a random password
- create password entries
- view saved entries
- update entries
- delete entries
- search by title or username

## GUI Screenshots

### Menu

![menu](iteration2_windowed_screenshots/gui-menu.png?raw=true)

### Create

![create](iteration2_windowed_screenshots/gui-create.png?raw=true)

### List

![list](iteration2_windowed_screenshots/gui-list.png?raw=true)

### Search

![search](iteration2_windowed_screenshots/gui-search.png?raw=true)

![search](iteration2_windowed_screenshots/gui-search-username.png?raw=true)

### Update

![update](iteration2_windowed_screenshots/gui-update.png?raw=true)

### Delete

![delete](iteration2_windowed_screenshots/gui-delete.png?raw=true)

### Required field validation

![invalid password](iteration2_windowed_screenshots/gui-password_error.png?raw=true)