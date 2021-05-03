from django.db import models
from hortum.users.models import User

class Productor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)