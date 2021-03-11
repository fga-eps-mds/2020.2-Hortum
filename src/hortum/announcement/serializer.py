from rest_framework import serializers
from .models import Announcement
from ..picture.serializer import PictureSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True)

    class Meta:
        model = Announcement
        fields = ['idPicture', 'likes', 'name', 'description', 'inventory'] 
