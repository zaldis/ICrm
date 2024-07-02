from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    user_id: int
    organization: str
