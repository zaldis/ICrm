from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from . import models


User = get_user_model()


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    search_fields = ('user__username', )
    list_filter = ('rate', 'specialization', )

    list_display = (
        'user',
        'rate',
        'specialization'
    )


@register(models.DeliveryManager)
class DeliveryManagerAdmin(admin.ModelAdmin):
    search_fields = ('user__username', )

    list_display = (
        'user',
    )


@register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('organisation', )

    list_display = (
        'organisation',
    )
