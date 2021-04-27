from django.db import models
from hortum.users.models import User

class Productor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Localization(models.Model):
    adress = models.CharField(max_length=100)
