from viewflow.contrib.auth import AuthViewset

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', AuthViewset(with_profile_view=False).urls),
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core'))
]
