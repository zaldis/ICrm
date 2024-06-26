from django.db import models

from user import models as user_models


class DeveloperRequest(models.Model):
    customer = models.ForeignKey(
        user_models.Customer,
        on_delete=models.CASCADE,
        related_name='request_processes',
        help_text='Customer who requested new developer',
    )
    specialization = models.CharField(
        max_length=30,
        choices=user_models.Developer.Specialization.choices,
        help_text="What specialization does the customer need",
    )
    grade = models.CharField(
        max_length=30,
        choices=user_models.Developer.Grades.choices,
        help_text="What grade does the customer need",
    )
    suggested_developers = models.ManyToManyField(
        user_models.Developer,
        related_name='request_processes',
        help_text='Developers who were suggested for this request by the delivery manager',
    )
    approved_developer = models.ForeignKey(
        user_models.Developer,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        related_name='approved_request_processes',
        help_text='Developers who was approved for this request by the customer',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
