import secrets
import string

from config.settings import DEFAULT_PASSWORD_LENGTH


def generate_password(length=DEFAULT_PASSWORD_LENGTH):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(secrets.choice(characters) for _ in range(length))