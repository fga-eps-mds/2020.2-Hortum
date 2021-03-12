from django.db import models
from rest_framework import serializers

from hortum.picture.models import Picture

class Announcement(models.Model):
    idPicture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    inventory = models.BooleanField(default=False)
