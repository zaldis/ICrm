from dataclasses import dataclass

from .user import User
from .delivery_manager import DeliveryManager


@dataclass
class Developer:
    user: User
    grade: str
    specialization: str
    delivery_manager: DeliveryManager | None
