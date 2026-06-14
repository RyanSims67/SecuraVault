from src.models.password_entry import PasswordEntry
from src.services.validation import validate_entry


class VaultService:
    def __init__(self):
        self.entries = []

    def create_entry(self, title, username, password):
        validate_entry(title, username, password)

        entry = PasswordEntry(
            title=title.strip(),
            username=username.strip(),
            password=password.strip()
        )

        self.entries.append(entry)
        return entry

    def view_entries(self):
        return self.entries

    def edit_entry(self, entry_id, title, username, password):
        validate_entry(title, username, password)

        entry = self.find_entry(entry_id)

        entry.title = title.strip()
        entry.username = username.strip()
        entry.password = password.strip()

        return entry

    def delete_entry(self, entry_id):
        entry = self.find_entry(entry_id)
        self.entries.remove(entry)

    def find_entry(self, entry_id):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry

        raise ValueError("Password entry not found.")