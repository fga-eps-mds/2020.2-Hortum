from django.db import models
from hortum.picture.models import Picture
from hortum.users.models import User

class Productor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)

class Localization(models.Model):
    adress = models.CharField(max_length=100)
