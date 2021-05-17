from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..validators import UniqueValidator
from .validators import PasswordValidator

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
        extra_kwargs = {'password': {'validators': [PasswordValidator()]}}

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username})
        data.update({'email': self.user.email})
        data.update({'phone_number': self.user.phone_number})
        data.update({'profile_picture': self.user.profile_picture.url})
        data.update({'is_productor': self.user.is_productor})
        return data

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, validators=[PasswordValidator(password='old_password')])
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'profile_picture']
        extra_kwargs = {
            'email': {'required': False, 'write_only': True, 'validators': [UniqueValidator(queryset=User.objects.all())]},
            'username': {'required': False, 'write_only': True},
            'phone_number': {'required': False, 'write_only': True, 'validators': [UniqueValidator(queryset=User.objects.all())]}
        }

    def validate(self, data):
        if len(data) == 0:
            raise serializers.ValidationError('Campos Vazios!')
        return data