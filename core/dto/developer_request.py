import datetime as dt
from dataclasses import dataclass

from user import dto as user_dto


@dataclass
class DeveloperRequest:
    id: int
    customer: user_dto.Customer
    specialization: str
    grade: str
    suggested_developers: list[user_dto.Developer]
    approved_developer: user_dto.Developer | None
    created_at: dt.datetime
    last_modified_at: dt.datetime
