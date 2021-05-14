from rest_framework import serializers

from .models import Productor
from ..users.models import User

from ..users.serializer import UserSerializer

class ProductorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Productor
        fields = ['user', 'announcements']
        read_only_fields = ['announcements']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data, is_productor=True)
        return Productor.objects.create(user=user, **validated_data)
        
class ProductorListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    profile_picture = serializers.ImageField(source='user.profile_picture')

    class Meta:
        model = Productor
        fields = ['username', 'email', 'phone_number', 'profile_picture']