from rest_framework import serializers

from django.db.models import Q

from .models import Announcement, AnnouncementImage, Localization
from ..productor.models import Productor
from ..validators import UniqueValidator

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(child=serializers.CharField(), write_only=True, max_length=3)
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Announcement
        fields = ['name', 'images', 'type_of_product', 'description', 'price', 'inventory', 'localizations', 'likes']
        extra_kwargs = {'name': {'validators': [UniqueValidator()]}}

    def create(self, validated_data):
        localizations = validated_data.pop('localizations')
        images = validated_data.pop('images')
        produtor_pk = Productor.objects.get(user__email=self.context['request'].user)
        announcement = Announcement.objects.create(idProductor=produtor_pk, **validated_data)
        [AnnouncementImage.objects.create(idImage=announcement, picture=picture) for picture in images]
        [Localization.objects.create(idAnnoun=announcement, adress=local) for local in localizations]
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(child=serializers.CharField(), write_only=True, max_length=3)

    class Meta:
        model = Announcement
        fields = ['name', 'type_of_product', 'description', 'price', 'inventory', 'localizations']
        extra_kwargs = {'name': {'validators': [UniqueValidator()]}}

    def update(self, instance, validated_data):
        if 'localizations' in validated_data:
            localizations = validated_data.pop('localizations')
            Localization.objects.filter(Q(idAnnoun=instance) & ~Q(adress=localizations)).delete()
            for local in localizations:
                if not instance.__class__.objects.filter(name=instance.name, localizations__adress=local).exists():
                    Localization.objects.create(idAnnoun=instance, adress=local)
            instance.save()
        return super().update(instance, validated_data)

class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ['picture']

class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, source='idProductor.user.username')
    email = serializers.EmailField(required=True, source='idProductor.user.email')
    localizations = serializers.SlugRelatedField(many=True, slug_field='adress', read_only=True)
    phone_number = serializers.CharField(required=True, source='idProductor.user.phone_number')
    pictureProductor = serializers.ImageField(required=True, source='idProductor.user.profile_picture')
    images = AnnouncementImageSerializer(many=True)
    
    class Meta:
        model = Announcement
        fields = ['email', 'username', 'phone_number', 'pictureProductor', 'name', 'images', 'type_of_product', 'description', 'price', 'localizations', 'likes']