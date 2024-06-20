from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class DeliveryManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_manager')


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='developer')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
