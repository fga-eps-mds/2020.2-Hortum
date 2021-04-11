from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_productor']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username})
        data.update({'email': self.user.email})
        data.update({'is_productor': self.user.is_productor})
        return data

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer para alterar endpoint da senha.
    """
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UpdateUserSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)