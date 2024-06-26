from user.models import DeliveryManager


def get_delivery_manager_by_user_id(user_id: int) -> DeliveryManager:
    return DeliveryManager.objects.filter(user_id=user_id).first()
