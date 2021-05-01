from rest_framework import serializers

from django.db.models import Q

from .models import Announcement, AnnouncementImage, Localization


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(child=serializers.CharField(), allow_empty=True, write_only=True)
    images = serializers.ListField(child=serializers.ImageField(), write_only=True, allow_empty=True)

    class Meta:
        model = Announcement
        fields = ['likes', 'name', 'type_of_product', 'description', 'price', 'inventory', 'localizations', 'images']

    def validate_name(self, name):
        if self.context['productor'].announcements.all().filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def create(self, validated_data):
        localizations = validated_data.pop('localizations')
        images = validated_data.pop('images')
        announcement = Announcement.objects.create(idProductor=self.context['productor'], **validated_data)
        [AnnouncementImage.objects.create(idImage=announcement, picture=picture) for picture in images]
        [Localization.objects.create(idAnnoun=announcement, adress=local) for local in localizations]
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(child=serializers.CharField(), allow_empty=True, write_only=True)

    class Meta:
        model = Announcement
        fields = ['name', 'type_of_product', 'description', 'price', 'inventory', 'localizations']

    def validate_name(self, name):
        if self.context['queryset'].filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def update(self, instance, validated_data):
        if 'localizations' in validated_data:
            localizations = validated_data.pop('localizations')
            Localization.objects.filter(Q(idAnnoun=instance) & ~Q(adress=localizations)).delete()
            for local in localizations:
                if not instance.__class__.objects.filter(localizations__adress=local).exists():
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
        fields = ['email', 'username', 'phone_number', 'pictureProductor', 'name', 'type_of_product', 'description', 'price', 'likes', 'images', 'localizations']
