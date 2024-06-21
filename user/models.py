from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    organisation = models.CharField(max_length=50)


class DeliveryManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_manager')
    customer = models.OneToOneField(
        Customer,
        on_delete=models.SET_NULL,
        related_name='delivery_manager',
        null=True,
        blank=True,
    )


class Developer(models.Model):

    class Rates(models.TextChoices):
        JUNIOR = 'T1', "Junior"
        MIDDLE = 'T2', "Middle"
        SENIOR = 'T3', "Senior"

    class Specialization(models.TextChoices):
        SOFTWARE_ENGINEERING = 'SE', "Software Engineering"
        DEV_OPS = 'DO', "DevOps"
        BIG_DATA = 'BD', "Big Data"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='developer')
    rate = models.CharField(max_length=10, choices=Rates.choices)
    specialization = models.CharField(max_length=30, choices=Specialization.choices)
    delivery_manager = models.ForeignKey(
        DeliveryManager,
        on_delete=models.SET_NULL,
        related_name='developers',
        null=True,
        blank=True,
    )
