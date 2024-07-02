from user.models import Developer
from user import dto


def get_developers_on_bench() -> list[dto.Developer]:
    return list(Developer.objects.filter(delivery_manager__isnull=True))
