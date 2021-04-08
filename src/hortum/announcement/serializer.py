from rest_framework import serializers

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User

from ..picture.serializer import PictureSerializer

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Announcement
        fields = ['email', 'idPicture', 'likes', 'name', 'type_of_product', 'description', 'price', 'inventory']

    def validate(self, data):
        productor = Productor.objects.get(user=User.objects.get(email=data['email']))
        if productor.announcements.filter(name=data['name']).exists():
            raise serializers.ValidationError({'name': 'Este nome de anúncio ja foi utilizado.'})
        return data

    def create(self, validated_data):
        productor_pk = Productor.objects.get(user=User.objects.get(email=validated_data.pop('email')))
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
