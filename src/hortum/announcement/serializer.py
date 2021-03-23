from rest_framework import serializers
from .models import Announcement
from ..picture.serializer import PictureSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['idPicture', 'likes', 'name', 'description', 'price', 'inventory'] 

    # def create(self, validated_data):
    #     return Announcement.objects.create(**validated_data)
