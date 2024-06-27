from user import models as user_models

from core.services.flow_process import get_flow_process_by_developer_request, get_flow_process_task
from . import spec


def run_start_node(
    requested_by: user_models.Customer,
    specialization: user_models.Developer.Specialization,
    grade: user_models.Developer.Grades
):
    spec.NewDeveloperRequestFlow.start.run(
        requested_by=requested_by,
        specialization=specialization,
        grade=grade,
    )


def run_approve_by_customer_node(developer_request, approved_developer):
    developer_request_process = get_flow_process_by_developer_request(developer_request)
    approve_task = get_flow_process_task(
        parent_process=developer_request_process,
        node=spec.NewDeveloperRequestFlow.approved_by_customer
    )
    spec.NewDeveloperRequestFlow.approved_by_customer.run(
        approve_task,
        approved_developer=approved_developer,
    )
