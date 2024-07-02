from user.models import Customer
from user import dto


def get_customer_by_user_id(user_id: int) -> dto.Customer:
    return Customer.objects.filter(user_id=user_id).first()
