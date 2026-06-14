import json

from src.models.password_entry import PasswordEntry
from src.services.encryption_service import EncryptionService
from src.storage.file_storage import FileStorage


def create_test_storage(tmp_path):
    vault_file = tmp_path / "vault.json"
    key_file = tmp_path / "test.key"

    encryption = EncryptionService(key_file)
    storage = FileStorage(vault_file, encryption)

    return storage, vault_file


def test_save_and_load_entry(tmp_path):
    storage, vault_file = create_test_storage(tmp_path)

    entry = PasswordEntry(
        title="GitHub",
        username="test@gmail.com",
        password="Test123!"
    )

    storage.save_entries([entry])
    loaded_entries = storage.load_entries()

    assert vault_file.exists()
    assert len(loaded_entries) == 1
    assert loaded_entries[0].title == "GitHub"
    assert loaded_entries[0].username == "test@gmail.com"
    assert loaded_entries[0].password == "Test123!"


def test_password_is_encrypted_in_file(tmp_path):
    storage, vault_file = create_test_storage(tmp_path)

    entry = PasswordEntry(
        title="Email",
        username="test2@gmail.com",
        password="Test321!"
    )

    storage.save_entries([entry])

    saved_data = json.loads(
        vault_file.read_text(encoding="utf-8")
    )

    assert saved_data[0]["password"] != "Test321!"


def test_missing_file_returns_empty_list(tmp_path):
    storage, vault_file = create_test_storage(tmp_path)

    assert not vault_file.exists()
    assert storage.load_entries() == []