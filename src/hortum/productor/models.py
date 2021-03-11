from django.db import models
from rest_framework import serializers

from hortum.announcement.models import Announcement
from hortum.picture.models import Picture
from hortum.users.models import User

class Productor(User):
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    idAnun = models.OneToOneField(Announcement, on_delete=models.CASCADE, null=True)

class Localization(models.Model):
    adress = models.CharField(max_length=100)
