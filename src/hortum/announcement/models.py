from django.db import models
from rest_framework import serializers

from ..productor.models import Productor
from hortum.picture.models import Picture

class Announcement(models.Model):
    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='announcements')
    idPicture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    inventory = models.BooleanField(default=False)
