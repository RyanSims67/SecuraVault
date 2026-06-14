def validate_entry(title, username, password):
    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not username.strip():
        raise ValueError("Username cannot be empty.")

    if not password.strip():
        raise ValueError("Password cannot be empty.")