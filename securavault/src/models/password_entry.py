from dataclasses import dataclass
from uuid import uuid4


@dataclass
class PasswordEntry:
    title: str
    username: str
    password: str
    entry_id: str = ""

    def __post_init__(self):
        if not self.entry_id:
            self.entry_id = str(uuid4())