from user.models import Customer


def get_customer_by_user_id(user_id: int) -> Customer | None:
    return Customer.objects.filter(user_id=user_id).first()
