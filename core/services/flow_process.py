from viewflow.workflow import Node
from viewflow.workflow.models import Process, Task
from django.db import models
from django.contrib.contenttypes.models import ContentType

from core.models import DeveloperRequest


def get_process_by_artifact(artifact_obj: models.Model) -> Process:
    artifact_type = ContentType.objects.get_for_model(type(artifact_obj))
    return Process.objects.get(
        artifact_content_type_id=artifact_type.id,
        artifact_object_id=artifact_obj.id
    )


def get_process_task(parent_process: Process, node: Node) -> Task:
    task = parent_process.task_set.get(flow_task=node)
    return task


def get_developer_request_process_by_developer_request(developer_request: DeveloperRequest) -> Process:
    return get_process_by_artifact(developer_request)

