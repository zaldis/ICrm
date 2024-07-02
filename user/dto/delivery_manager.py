from dataclasses import dataclass

from .user import User
from .customer import Customer


@dataclass
class DeliveryManager:
    user_id: int
    user: User
    customer: Customer | None
