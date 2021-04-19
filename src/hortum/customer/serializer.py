from rest_framework import serializers

from .models import Customer
from ..productor.models import Productor
from ..announcement.models import Announcement
from ..users.models import User

from ..users.serializer import UserSerializer
from ..picture.serializer import PictureSerializer
from ..announcement.serializer import AnnouncementListSerializer, AnnouncementFavSerializer
from ..productor.serializer import ProductorListSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    idPicture = PictureSerializer(read_only=True)
    idAnunFav = AnnouncementListSerializer(many=True, read_only=True)
    idProdFav = ProductorListSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['user', 'idPicture', 'idAnunFav', 'idProdFav']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Customer.objects.create(user=user, **validated_data)

class CustomerAddAnnouncementSerializer(serializers.ModelSerializer):
    announcementName = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ['email', 'announcementName']

    def validate_email(self, email):
        if not Productor.objects.filter(user__email=email).exists():
            raise serializers.ValidationError('Email de produtor inexistente')
        return email

    def validate_announcementName(self, name):
        if not Announcement.objects.filter(name=name).exists():
            raise serializers.ValidationError('Nome de anúncio inexistente')
        return name

class CustomerFavoritesAnnouncementsSerializer(serializers.ModelSerializer):
    idAnunFav = AnnouncementFavSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['idAnunFav']

class CustomerFavoritesProductorsSerializer(serializers.ModelSerializer):
    idProdFav = ProductorListSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['idProdFav']