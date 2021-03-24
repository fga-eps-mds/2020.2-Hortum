from rest_framework import serializers

from .models import Productor, Localization
from ..users.models import User

from ..users.serializer import UserSerializer
from ..picture.serializer import PictureSerializer
from ..announcement.serializer import AnnouncementSerializer

class ProductorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    idPicture = PictureSerializer(many=False, read_only=True)
    idAnun = AnnouncementSerializer(many=True, read_only=True)

    class Meta:
        model = Productor
        fields = ['user', 'idPicture', 'idAnun']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, is_productor=True)
        return Productor.objects.create(user=user, **validated_data)

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ['adress']
