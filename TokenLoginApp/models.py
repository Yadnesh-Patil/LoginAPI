# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import AppConfig


class CustomUser(AbstractUser):
    # Add additional fields here
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.username
