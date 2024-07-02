from user.models import DeliveryManager
from user import dto


def get_delivery_manager_by_user_id(user_id: int) -> dto.DeliveryManager:
    return DeliveryManager.objects.filter(user_id=user_id).first()
