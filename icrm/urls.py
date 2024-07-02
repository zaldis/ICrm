from django.contrib import admin
from django.urls import path, include
from viewflow.urls import Site, Application
from viewflow.workflow.flow import FlowAppViewset

from core.flows.developer_request.spec import NewDeveloperRequestFlow


site = Site(title="iCRM", viewsets=[
    Application(
        title='Developer Request',
        icon='person_add',
        app_name='admin-flow',
        viewsets=[
            FlowAppViewset(NewDeveloperRequestFlow),
        ]
    ),
])


urlpatterns = [
    path('admin/business-flow/', site.urls),
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
]
