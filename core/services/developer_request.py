from user import models as user_models
from core.models import DeveloperRequest


def create_new_developer_request(
    *,
    requested_by: user_models.Customer,
    specialization: user_models.Developer.Specialization,
    grade: user_models.Developer.Grades,
) -> DeveloperRequest:
    developer_request = DeveloperRequest.objects.create(
        customer=requested_by,
        specialization=specialization,
        grade=grade,
    )
    return developer_request


def get_developer_request_by_id(developer_request_id: int) -> DeveloperRequest:
    return DeveloperRequest.objects.get(id=developer_request_id)


def get_active_developer_request(customer_id: int) -> DeveloperRequest | None:
    try:
        return DeveloperRequest.objects.get(
            customer_id=customer_id,
            approved_developer=None,
        )
    except DeveloperRequest.DoesNotExist:
        return None


def get_passed_developer_requests(customer_id: int) -> list[DeveloperRequest]:
    return DeveloperRequest.objects.filter(
        customer_id=customer_id,
        approved_developer__isnull=False,
    ).order_by("-last_modified_at")


def suggest_new_developer(developer_request: DeveloperRequest, suggested_developer: user_models.Developer) -> None:
    developer_request.suggested_developers.add(suggested_developer)


def cancel_suggested_developer(developer_request: DeveloperRequest, cancelled_developer: user_models.Developer) -> None:
    developer_request.suggested_developers.remove(cancelled_developer)


def approve_developer(developer_request: DeveloperRequest, approved_developer: user_models.Developer):
    developer_request.approved_developer = approved_developer
    developer_request.save()
    _link_developer_to_customer(developer_request)


def _link_developer_to_customer(developer_request: DeveloperRequest):
    developer = developer_request.approved_developer
    customer = developer_request.customer

    developer.delivery_manager = customer.delivery_manager
    developer.save()
