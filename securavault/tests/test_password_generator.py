import pytest

from config.settings import DEFAULT_PASSWORD_LENGTH
from src.services.password_generator import generate_password


def test_default_password_length():
    password = generate_password()

    assert len(password) == DEFAULT_PASSWORD_LENGTH


def test_custom_password_length():
    password = generate_password(14)

    assert len(password) == 14


def test_short_password_raises_error():
    with pytest.raises(
        ValueError,
        match="Password length must be at least 8"
    ):
        generate_password(5)