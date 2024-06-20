from django.urls import path

from core.views import IndexView, LoginView


app_name = 'core'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
]
