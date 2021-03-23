from rest_framework import serializers

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User

from ..picture.serializer import PictureSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Announcement
        fields = ['email', 'idPicture', 'likes', 'name', 'type_of_product', 'description', 'price', 'inventory'] 

    def create(self, validated_data):
        productor_pk = Productor.objects.get(user=User.objects.get(email=validated_data.pop('email')))
        announcement = Announcement.objects.create(idProductor=productor_pk, **validated_data)
        return announcement
