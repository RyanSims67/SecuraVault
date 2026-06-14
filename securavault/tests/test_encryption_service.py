from src.services.encryption_service import EncryptionService


def test_encrypts_password(tmp_path):
    key_file = tmp_path / "test.key"
    service = EncryptionService(key_file)

    encrypted_password = service.encrypt("Test123!")

    assert encrypted_password != "Test123!"


def test_decrypts_password(tmp_path):
    key_file = tmp_path / "test.key"
    service = EncryptionService(key_file)

    encrypted_password = service.encrypt("Test123!")
    decrypted_password = service.decrypt(encrypted_password)

    assert decrypted_password == "Test123!"


def test_creates_key_file(tmp_path):
    key_file = tmp_path / "test.key"

    EncryptionService(key_file)

    assert key_file.exists()