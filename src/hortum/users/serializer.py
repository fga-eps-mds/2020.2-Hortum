from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']

class UserDeleteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['password']

    def validate_password(self, password):
        if not self.context['user'].check_password(password):
            raise serializers.ValidationError('Senha incorreta!')
        return password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username})
        data.update({'email': self.user.email})
        data.update({'is_productor': self.user.is_productor})
        data.update({'profile_picture': self.user.profile_picture.url})
        return data

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate_old_password(self, old_password):
        if not self.context['user'].check_password(old_password):
            raise serializers.ValidationError('Senha incorreta!')
        return old_password


class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, write_only=True)
    email = serializers.EmailField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate(self, data):
        if len(data) == 0:
            raise serializers.ValidationError('Campos Vazios!')
        return data

    def validate_email(self, email):
        if self.context['queryset'].filter(email=email).exists():
            raise serializers.ValidationError('Email ja registrado!')
        return email