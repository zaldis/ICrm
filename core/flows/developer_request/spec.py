from viewflow import this
from viewflow.workflow import flow, Activation
from viewflow.workflow.models import Process

from core.services import developer_request as developer_request_service


class NewDeveloperRequestFlow(flow.Flow):
    start = flow.StartHandle(
        this.start_process_handler
    ).Next(this.approved_by_customer)

    approved_by_customer = flow.Handle(
        this.approved_by_customer_handler
    ).Next(this.end)

    end = flow.End()

    def start_process_handler(
        self,
        activation: Activation,
        customer_id: int,
        specialization: str,
        grade: str,
    ) -> Process:
        developer_request = developer_request_service.create_new_developer_request(
            customer_id=customer_id,
            specialization=specialization,
            grade=grade
        )
        activation.process.artifact = developer_request
        return activation.process

    def approved_by_customer_handler(
        self,
        activation: Activation,
        approved_developer_id: int,
    ) -> Process:
        developer_request = activation.process.artifact
        developer_request_service.approve_developer(developer_request.id, approved_developer_id)
        return activation.process
