[Back to DDD Doc](ddd.md)

# Domains


| Domain | Description | Related Events | Related Requirements |
|---|---|---|---|
| Vault Management | Handles creating, viewing, editing, deleting, and searching password entries. | Password entry created, viewed, edited, deleted, searched | F1, F2, F3, F4, F6 |
| Encryption | Encrypts password data before storage and keeps encryption logic separate from vault logic. | Password entry encrypted, encryption settings changed | S1, Q2 |
| Password Generation | Generates strong random passwords and allows generator settings to change. | Strong random password generated, password generator settings changed | F5, Q1 |
| Storage | Saves and loads encrypted password data. | Password data stored | S1 |
| Testing / Quality Assurance | Supports automated testing for the core password manager logic. | Automated tests executed | Q3 |


## Future Domains

These domains are included to show how SecuraVault could grow into a larger system. They are not part of the current implementation.

| Domain | Description |
|---|---|
| Authentication | Unlocks the vault using a master password and controls access. |
| Password Strength Analysis | Evaluates password strength and warns about weak passwords. |
| Backup and Export | Creates backups and exports vault data securely. |
| Audit Log | Records important security-related actions. |
| Notifications | Reminds users about weak, old, or compromised passwords. |


## Explanation

The main domain is Vault Management because most user actions happen there. 

Encryption is separated because security rules should not be mixed directly into storage or user interface logic. 

Password Generation is separated because generator settings may change independently. 

Storage is separated because saving and loading data is a technical responsibility. 

Testing / Quality Assurance is separated because tests support the project but should not become part of the production domain logic.