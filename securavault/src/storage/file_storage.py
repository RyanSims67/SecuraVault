import json
from pathlib import Path

from config.settings import STORAGE_FILE
from src.models.password_entry import PasswordEntry
from src.services.encryption_service import EncryptionService


class FileStorage:
    def __init__(self, file_path=STORAGE_FILE, encryption=None):
        self.file_path = Path(file_path)
        self.encryption = encryption or EncryptionService()

    def save_entries(self, entries):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = []

        for entry in entries:
            data.append({
                "entry_id": entry.entry_id,
                "title": entry.title,
                "username": entry.username,
                "password": self.encryption.encrypt(entry.password)
            })

        self.file_path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )

    def load_entries(self):
        if not self.file_path.exists():
            return []

        file_content = self.file_path.read_text(encoding="utf-8")

        if not file_content.strip():
            return []

        data = json.loads(file_content)
        entries = []

        for item in data:
            entry = PasswordEntry(
                title=item["title"],
                username=item["username"],
                password=self.encryption.decrypt(item["password"]),
                entry_id=item["entry_id"]
            )

            entries.append(entry)

        return entries