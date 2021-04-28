from rest_framework import serializers

from .models import Announcement, AnnouncementImage


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Announcement
        fields = ['likes', 'name', 'type_of_product', 'description', 'price', 'inventory', 'images']

    def validate_name(self, name):
        if self.context['productor'].announcements.all().filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def create(self, validated_data):
        images = validated_data.pop('images')
        productor_pk = self.context['productor']
        announcement = Announcement.objects.create(idProductor=productor_pk, **validated_data)
        [AnnouncementImage.objects.create(idImage=announcement, picture=picture) for picture in images]
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def validate_name(self, name):
        if self.context['queryset'].filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ['picture']

class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, source='idProductor.user.username')
    email = serializers.EmailField(required=True, source='idProductor.user.email')
    pictureProductor = serializers.ImageField(required=True, source='idProductor.user.profile_picture')
    images = AnnouncementImageSerializer(many=True)

    class Meta:
        model = Announcement
        fields = ['email', 'username', 'pictureProductor', 'name', 'type_of_product', 'description', 'price', 'likes', 'images']
