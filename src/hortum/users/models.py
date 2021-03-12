from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=120)
    password = models.CharField(max_length=110)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
