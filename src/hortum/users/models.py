from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=120)
    phone_number = models.CharField(unique=True, blank=False, null=True, max_length=13)
    is_productor = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
