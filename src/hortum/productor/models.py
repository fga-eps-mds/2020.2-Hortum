from django.db import models
from rest_framework import serializers

from hortum.announcement.models import Announcement
from hortum.picture.models import Picture
from hortum.users.models import User

class Productor(User):
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    idAnun = models.OneToOneField(Announcement, on_delete=models.CASCADE, null=True)

class ProductorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    idPicture = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    idAnun = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class Localization(models.Model):
    adress = models.CharField(max_length=100)

class LocalizationSerializer(serializers.Serializer):
    adress = serializers.CharField(max_length=100)
