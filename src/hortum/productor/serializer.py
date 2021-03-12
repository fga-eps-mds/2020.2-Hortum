from rest_framework import serializers

from .models import Productor, Localization

from ..users.serializer import UserSerializer
from ..picture.serializer import PictureSerializer
from ..announcement.serializer import AnnouncementSerializer

class ProductorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    idPicture = PictureSerializer(many=False, read_only=True)
    idAnunFav = AnnouncementSerializer(many=True, read_only=True)

    class Meta:
        model = Productor
        fields = ['user', 'idPicture', 'idAnun']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Productor.objects.create(user=user, **validated_data)

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ['adress']
