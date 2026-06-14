from pathlib import Path

from cryptography.fernet import Fernet

from config.settings import ENCRYPTION_KEY_FILE


class EncryptionService:
    def __init__(self, key_file=ENCRYPTION_KEY_FILE):
        self.key_file = Path(key_file)
        self.key = self._load_or_create_key()
        self.cipher = Fernet(self.key)

    def _load_or_create_key(self):
        self.key_file.parent.mkdir(parents=True, exist_ok=True)

        if self.key_file.exists():
            return self.key_file.read_bytes()

        key = Fernet.generate_key()
        self.key_file.write_bytes(key)
        return key

    def encrypt(self, text):
        encrypted_text = self.cipher.encrypt(text.encode())
        return encrypted_text.decode()

    def decrypt(self, encrypted_text):
        decrypted_text = self.cipher.decrypt(encrypted_text.encode())
        return decrypted_text.decode()