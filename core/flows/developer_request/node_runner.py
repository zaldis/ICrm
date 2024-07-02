from core.services.flow_process import get_flow_process_by_developer_request, get_flow_process_task
from . import spec


def run_start_node(customer_id: int, specialization: str, grade: str):
    spec.NewDeveloperRequestFlow.start.run(
        customer_id=customer_id,
        specialization=specialization,
        grade=grade,
    )


def run_approve_by_customer_node(
    developer_request_id: int,
    approved_developer_id: int,
):
    developer_request_process = get_flow_process_by_developer_request(developer_request_id)
    approve_task = get_flow_process_task(
        parent_process=developer_request_process,
        node=spec.NewDeveloperRequestFlow.approved_by_customer
    )
    spec.NewDeveloperRequestFlow.approved_by_customer.run(
        approve_task,
        approved_developer_id=approved_developer_id,
    )
