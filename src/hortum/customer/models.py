from django.db import models
from rest_framework import serializers

from hortum.productor.models import Productor
from hortum.picture.models import Picture
from hortum.announcement.models import Announcement
from hortum.users.models import User

class Customer(User):
    idPicture = models.OneToOneField(Picture, on_delete=models.CASCADE, null=True)
    idAnunFav = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True)
    idProdFav = models.ForeignKey(Productor, on_delete=models.CASCADE, null=True) 

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    idPicture = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    idAnunFav = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    idProdFav = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 