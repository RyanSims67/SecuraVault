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
| Generate password | A random password is generated. | Not tested yet |
| Password length setting | The generated password uses the configured length. | Not tested yet |
| Password character settings | The generated password can use configured character groups. | Not tested yet |
| Encrypt password | A plain password is converted into an encrypted value. | Not tested yet |
| Encrypted value differs from plain text | The stored encrypted value is not the same as the original password. | Not tested yet |
| Decrypt password | The encrypted value can be decrypted when needed. | Not tested yet |
| Search by title | Matching entries can be found by title. | Not tested yet |
| Search by username | Matching entries can be found by username. | Not tested yet |
| Separation of encryption logic | Encryption code is kept separate from vault entry logic. | Not tested yet |
