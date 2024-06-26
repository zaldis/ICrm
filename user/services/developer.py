from user.models import Developer


def get_developers_on_bench() -> list[Developer]:
    return list(Developer.objects.filter(delivery_manager__isnull=True))
