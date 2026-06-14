[Back to Main Doc](../../README.md)

# Clean Code Development

I reviewed my SecuraVault code and selected examples that made the project easier for me to understand, test and change.

## Example 1 — Clear Function Names

Location: [vault_service.py](../../securavault/src/services/vault_service.py)

```text
securavault/src/services/vault_service.py
```

Examples:

```python
def create_entry(self, title, username, password):

def edit_entry(self, entry_id, title, username, password):

def delete_entry(self, entry_id):

def search_entries(self, search_text):
```

I used names that clearly explain what each function does.

This helped me connect the CLI and GUI to the correct vault operation without needing extra comments.

## Example 2 — Separate Validation

Location: [validation.py](../../securavault/src/services/validation.py)

```text
securavault/src/services/validation.py
```

```python
def validate_entry(title, username, password):
    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not username.strip():
        raise ValueError("Username cannot be empty.")

    if not password.strip():
        raise ValueError("Password cannot be empty.")
```

I kept the input validation in a separate file instead of repeating the same checks in several functions.

This made the validation rules easier to find and reduced duplicated code.

## Example 3 — Separate Encryption Logic

Location: [encryption_service.py](../../securavault/src/services/encryption_service.py)

```text
securavault/src/services/encryption_service.py
```

```python
def encrypt(self, text):
    encrypted_text = self.cipher.encrypt(text.encode())
    return encrypted_text.decode()


def decrypt(self, encrypted_text):
    decrypted_text = self.cipher.decrypt(encrypted_text.encode())
    return decrypted_text.decode()
```

Encryption is handled by its own service instead of being mixed into the vault, storage or interface code.

This made the encryption behaviour easier for me to understand and test separately.

## Example 4 — Separate File Storage

Location: [file_storage.py](../../securavault/src/storage/file_storage.py)

```text
securavault/src/storage/file_storage.py
```

The `FileStorage` class is responsible for saving and loading password entries.

`VaultService` manages the entries, while `FileStorage` manages the JSON file.

This separation allowed me to test the vault using `FakeStorage` and `Mock` without changing my real `vault.json` file.

## Example 5 — Configuration Values

Location: [settings.py](../../securavault/config/settings.py)

```text
securavault/config/settings.py
```

```python
DEFAULT_PASSWORD_LENGTH = 10
ENCRYPTION_KEY_FILE = "data/secret.key"
STORAGE_FILE = "data/vault.json"
```

I stored settings such as file locations and the default password length in one file.

This avoided repeating the same values in several files and made the values easier to change.

## Example 6 — Small GUI Functions

Location: [gui.py](../../securavault/src/ui/gui.py)

```text
securavault/src/ui/gui.py
```

The GUI uses separate functions such as:

```python
create_entry()
update_entry()
delete_entry()
search_entries()
clear_fields()
```

Each function performs one main task.

This was easier for me to understand than placing every button action inside one large function.

# My CCD Cheat Sheet

These are the clean-code rules I would try to follow in future projects:

1. Use names that explain what a function or variable represents.
2. Keep functions focused on one main task.
3. Avoid repeating the same code in several places.
4. Separate user interface code from program logic.
5. Keep file-storage code separate from business logic.
6. Keep encryption and security logic in its own service.
7. Store configuration values in one place.
8. Validate user input before processing it.
9. Use error messages that explain what went wrong.
10. Keep code formatting consistent.
11. Remove code that is no longer used.
12. Write tests for important behaviour and error cases.

## What I Learned

The clearest improvement for me was separating the project into services, storage and user interface folders. Including using multiple different functions for the different services instead of one large function.

At first, placing everything inside one file would have been quicker. However, the separate files made automated testing and later changes easier.
