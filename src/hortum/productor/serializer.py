from rest_framework import serializers

from .models import Productor, Localization
from ..users.models import User

from ..users.serializer import UserSerializer
from ..announcement.serializer import AnnouncementCreateSerializer
from ..picture.serializer import PictureSerializer

class ProductorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    idPicture = PictureSerializer(many=False, read_only=True)
    announcements = AnnouncementCreateSerializer(read_only=True, many=True)

    class Meta:
        model = Productor
        fields = ['user', 'idPicture', 'announcements']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, is_productor=True)
        return Productor.objects.create(user=user, **validated_data)

class ProductorListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    idPicture = PictureSerializer()

    class Meta:
        model = Productor
        fields = ['username', 'email', 'idPicture']

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ['adress']
