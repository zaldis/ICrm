from django.urls import path

from django.contrib.auth import views as auth_views

from core.views import (
    IndexView,
    ProfileView,
    DeveloperRequestView,
    DeveloperApproveView,
    SuggestedDeveloperView,
)


app_name = 'core'


urlpatterns = [
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('developer-requests/', DeveloperRequestView.as_view(), name='developer-requests'),
    # path('developer-requests/<int:id>', DetailDeveloperRequestView.as_view(), name='detail-developer-request'),
    path(
        'developer-requests/<int:developer_request_id>/suggestion',
        SuggestedDeveloperView.as_view(),
        name='suggested-developer',
    ),
    path(
        'developer-requests/<int:developer_request_id>/approve',
        DeveloperApproveView.as_view(),
        name='approved-developer',
    ),

    path('', IndexView.as_view(), name='index'),
]
