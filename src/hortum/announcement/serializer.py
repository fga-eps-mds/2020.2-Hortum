from rest_framework import serializers

from .models import Announcement


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['likes', 'name', 'type_of_product', 'description', 'price', 'inventory', 'images']

    def validate_name(self, name):
        if self.context['productor'].announcements.all().filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def create(self, validated_data):
        productor_pk = self.context['productor']
        announcement = Announcement.objects.create(idProductor=productor_pk, **validated_data)
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def validate_name(self, name):
        if self.context['queryset'].filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, source='idProductor.user.username')
    email = serializers.EmailField(required=True, source='idProductor.user.email')
    pictureProductor = serializers.ImageField(required=True, source='idProductor.user.profile_picture')

    class Meta:
        model = Announcement
        fields = ['email', 'username', 'pictureProductor', 'name', 'type_of_product', 'description', 'price', 'likes', 'images']
