from rest_framework import serializers

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User

from ..picture.serializer import PictureSerializer

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['idPicture', 'likes', 'name', 'type_of_product', 'description', 'price', 'inventory'] 

    def validate_name(self, name):
        if self.context['productor'].announcements.all().filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def create(self, validated_data):
        productor_pk = self.context['productor']
        announcement = Announcement.objects.create(idProductor=productor_pk, **validated_data)
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = '__all__'

    def validate_name(self, name):
        if self.context['queryset'].filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name
