from dataclasses import dataclass


@dataclass
class User:
    username: str
    first_name: str | None
    last_name: str | None
