from django.db import models
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from hortum.picture.models import Picture


class Announcement(models.Model):
    idPicture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    inventory = models.BooleanField(default=False)

class AnnouncementSerializer(serializers.Serializer):
    idPicture = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    likes = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=200)
    inventory = serializers.BooleanField(default=False)

    def toJson(self):
        return JSONRenderer().render(self.data)