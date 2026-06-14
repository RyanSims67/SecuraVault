[Back to Main Doc](../../README.md)

# Testing

This document describes the automated testing used for SecuraVault.

The tests were created during Iteration 3 using pytest.

[Iteration 3](../Requirements/specifications_validation/iteration_3.md)

## Tests Added

I created tests for:
- creating, editing and deleting entries
- searching by title and username
- rejecting empty input
- handling an invalid entry ID
- generating passwords
- encrypting and decrypting passwords
- saving and loading entries
- checking that passwords are encrypted in the JSON file


| Test Files |
|---|
| [test_vault_service.py](../../securavault/tests/test_vault_service.py) |
| [test_password_generator.py](../../securavault/tests/test_password_generator.py) | 
| [test_encryption_service.py](../../securavault/tests/test_encryption_service.py) | 
| [test_file_storage.py](../../securavault/tests/test_file_storage.py) | 


I ran the complete tests from inside the securavault folder:

```text
python -m pytest -v

E.g. python -m pytest tests/test_vault_service.py -v   
```

![coverage](screenshots/coverage.png?raw=true)


## Test written without AI

```text
def test_new_vault_starts_empty():
    vault = create_vault()

    assert vault.view_entries() == []
```

This test creates a new vault using the test storage and checks that it initially contains no password entries.


## Test written with AI

Prompt used: Create a simple pytest test that checks whether deleting an entry with an invalid ID raises a ValueError.

```text
def test_invalid_id_raises_error(): 
    vault = create_vault() 
    
    with pytest.raises( 
        ValueError, 
        match="Password entry not found" 
    ): 
        vault.delete_entry("wrong-id")
```

The test passed when the expected `ValueError` was raised.



## Mock test - Storage

This mock test checks that the storage service is called after a new password entry is created.

```text
def test_mock_storage_save():
    storage = Mock()
    storage.load_entries.return_value = []

    vault = VaultService(storage)

    vault.create_entry(
        "GitHub",
        "test@gmail.com",
        "Test123!"
    )

    storage.save_entries.assert_called_once()
```

![Mock test passed](screenshots/coverage.png?raw=true)
