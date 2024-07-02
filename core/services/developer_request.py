from core import models as core_models
from core import dto as core_dto


def create_new_developer_request(
    *,
    customer_id: int,
    specialization: str,
    grade: str,
) -> core_dto.DeveloperRequest:
    developer_request = core_models.DeveloperRequest.objects.create(
        customer_id=customer_id,
        specialization=specialization,
        grade=grade,
    )
    return developer_request


def get_developer_request_by_id(developer_request_id: int) -> core_dto.DeveloperRequest:
    return core_models.DeveloperRequest.objects.get(id=developer_request_id)


def get_active_developer_request(customer_id: int) -> core_dto.DeveloperRequest | None:
    try:
        return core_models.DeveloperRequest.objects.get(
            customer_id=customer_id,
            approved_developer=None,
        )
    except core_models.DeveloperRequest.DoesNotExist:
        return None


def get_passed_developer_requests(customer_id: int) -> list[core_dto.DeveloperRequest]:
    return list(
        core_models.DeveloperRequest.objects.filter(
            customer_id=customer_id,
            approved_developer__isnull=False,
        ).order_by("-last_modified_at")
    )


def suggest_new_developer(developer_request_id: int, suggested_developer_id: int) -> None:
    developer_request_db_item = core_models.DeveloperRequest.objects.get(id=developer_request_id)
    developer_request_db_item.suggested_developers.add(suggested_developer_id)


def cancel_suggested_developer(developer_request_id: int, cancelled_developer_id: int) -> None:
    developer_request_db_item = core_models.DeveloperRequest.objects.get(id=developer_request_id)
    developer_request_db_item.suggested_developers.remove(cancelled_developer_id)


def approve_developer(developer_request_id: int, approved_developer_id: int):
    developer_request_db_item = core_models.DeveloperRequest.objects.get(id=developer_request_id)
    developer_request_db_item.approved_developer_id = approved_developer_id
    developer_request_db_item.save()
    _link_developer_to_customer(developer_request_db_item)


def _link_developer_to_customer(developer_request: core_models.DeveloperRequest):
    developer = developer_request.approved_developer
    customer = developer_request.customer

    developer.delivery_manager = customer.delivery_manager
    developer.save()
