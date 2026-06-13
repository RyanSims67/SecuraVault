from dataclasses import dataclass, asdict
from uuid import uuid4


@dataclass
class PasswordEntry:
    title: str
    username: str
    password: str
    entry_id: str = ""

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Title cannot be empty.")

        if not self.entry_id:
            self.entry_id = str(uuid4())

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "PasswordEntry":
        return cls(
            entry_id=data["entry_id"],
            title=data["title"],
            username=data["username"],
            password=data["password"],
        )