from rest_framework import serializers

from .models import Productor, Localization
from ..users.models import User

from ..users.serializer import UserSerializer
from ..announcement.serializer import AnnouncementCreateSerializer, AnnouncementListSerializer

class ProductorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    announcements = AnnouncementCreateSerializer(read_only=True, many=True)

    class Meta:
        model = Productor
        fields = ['user', 'announcements']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, is_productor=True)
        return Productor.objects.create(user=user, **validated_data)

class ProductorRetrieveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    announcements = AnnouncementListSerializer(many=True)
    profile_picture = serializers.ImageField(source='user.profile_picture')

    class Meta:
        model = Productor
        fields = ['username', 'email', 'announcements', 'profile_picture']
        
class ProductorListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    profile_picture = serializers.ImageField(source='user.profile_picture')

    class Meta:
        model = Productor
        fields = ['username', 'email', 'profile_picture']

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ['adress']
