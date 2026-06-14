import pytest
from unittest.mock import Mock

from src.services.vault_service import VaultService


class FakeStorage:
    def __init__(self):
        self.entries = []

    def load_entries(self):
        return self.entries

    def save_entries(self, entries):
        self.entries = list(entries)


def create_vault():
    storage = FakeStorage()
    return VaultService(storage)


def test_create_entry():
    vault = create_vault()

    entry = vault.create_entry(
        "GitHub",
        "test@gmail.com",
        "Test123!"
    )

    assert entry.title == "GitHub"
    assert entry.username == "test@gmail.com"
    assert entry.password == "Test123!"
    assert len(vault.view_entries()) == 1


def test_edit_entry():
    vault = create_vault()

    entry = vault.create_entry(
        "GitHub",
        "test@gmail.com",
        "Test123!"
    )

    vault.edit_entry(
        entry.entry_id,
        "GitHub Account",
        "updated@gmail.com",
        "Updated123!"
    )

    assert entry.title == "GitHub Account"
    assert entry.username == "updated@gmail.com"
    assert entry.password == "Updated123!"


def test_delete_entry():
    vault = create_vault()

    entry = vault.create_entry(
        "GitHub",
        "test@gmail.com",
        "Test123!"
    )

    vault.delete_entry(entry.entry_id)

    assert vault.view_entries() == []


def test_search_entry_by_title():
    vault = create_vault()

    vault.create_entry(
        "GitHub",
        "test@gmail.com",
        "Test123!"
    )

    results = vault.search_entries("git")

    assert len(results) == 1
    assert results[0].title == "GitHub"


def test_search_entry_by_username():
    vault = create_vault()

    vault.create_entry(
        "Email",
        "test@gmail.com",
        "Test123!"
    )

    results = vault.search_entries("test")

    assert len(results) == 1
    assert results[0].username == "test@gmail.com"


def test_empty_title_raises_error():
    vault = create_vault()

    with pytest.raises(ValueError):
        vault.create_entry(
            "",
            "test@gmail.com",
            "Test123!"
        )


def test_invalid_id_raises_error():
    vault = create_vault()

    with pytest.raises(
        ValueError,
        match="Password entry not found"
    ):
        vault.delete_entry("wrong-id")


def test_new_vault_starts_empty():
    vault = create_vault()

    assert vault.view_entries() == []


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