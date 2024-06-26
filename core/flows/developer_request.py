from viewflow import this
from viewflow.workflow import flow, Activation
from viewflow.workflow.models import Process

from core import models as core_models
from user import models as user_models
from core.services.developer_request import create_new_developer_request, approve_developer


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
        requested_by: user_models.Customer,
        specialization: user_models.Developer.Specialization,
        grade: user_models.Developer.Grades
    ) -> Process:
        developer_request = create_new_developer_request(
            requested_by=requested_by,
            specialization=specialization,
            grade=grade
        )
        activation.process.artifact = developer_request
        return activation.process

    def approved_by_customer_handler(
        self,
        activation: Activation,
        approved_developer: user_models.Developer
    ) -> Process:
        developer_request: core_models.DeveloperRequest = activation.process.artifact
        approve_developer(developer_request, approved_developer)
        return activation.process
