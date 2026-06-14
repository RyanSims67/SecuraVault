from src.models.password_entry import PasswordEntry
from src.services.validation import validate_entry
from src.storage.file_storage import FileStorage


class VaultService:
    def __init__(self, storage=None):
        self.storage = storage or FileStorage()
        self.entries = self.storage.load_entries()

    def create_entry(self, title, username, password):
        validate_entry(title, username, password)

        entry = PasswordEntry(
            title=title.strip(),
            username=username.strip(),
            password=password.strip()
        )

        self.entries.append(entry)
        self.save_entries()

        return entry

    def view_entries(self):
        return self.entries

    def edit_entry(self, entry_id, title, username, password):
        validate_entry(title, username, password)

        entry = self.find_entry(entry_id)

        entry.title = title.strip()
        entry.username = username.strip()
        entry.password = password.strip()

        self.save_entries()

        return entry

    def delete_entry(self, entry_id):
        entry = self.find_entry(entry_id)
        self.entries.remove(entry)

        self.save_entries()

    def search_entries(self, search_text):
        search_text = search_text.strip().lower()

        if not search_text:
            return []

        results = []

        for entry in self.entries:
            title_matches = search_text in entry.title.lower()
            username_matches = search_text in entry.username.lower()

            if title_matches or username_matches:
                results.append(entry)

        return results

    def find_entry(self, entry_id):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry

        raise ValueError("Password entry not found.")

    def save_entries(self):
        self.storage.save_entries(self.entries)