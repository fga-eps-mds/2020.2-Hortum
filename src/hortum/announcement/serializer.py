from rest_framework import serializers

from django.db.models import Q

from .models import Announcement, Localization

from ..picture.serializer import PictureSerializer

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)
    localizations = serializers.ListField(child=serializers.CharField(), allow_empty=True, write_only=True)

    class Meta:
        model = Announcement
        fields = ['idPicture', 'likes', 'name', 'type_of_product', 'description', 'price', 'inventory', 'localizations']

    def validate_name(self, name):
        if self.context['productor'].announcements.all().filter(name=name).exists():
            raise serializers.ValidationError('Este nome de anúncio ja foi utilizado.')
        return name

    def create(self, validated_data):
        localizations = validated_data.pop('localizations')
        announcement = Announcement.objects.create(idProductor=self.context['productor'], **validated_data)
        [Localization.objects.create(idAnnoun=announcement, adress=local) for local in localizations]
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(many=True, read_only=True)
    localizations = serializers.ListField(child=serializers.CharField(), allow_empty=True, write_only=True)

    class Meta:
        model = Announcement
        fields = ['idPicture', 'name', 'type_of_product', 'description', 'price', 'inventory', 'localizations']

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
        super().update(instance, validated_data)
        return instance

class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, source='idProductor.user.username')
    email = serializers.EmailField(required=True, source='idProductor.user.email')
    idPictureProductor = PictureSerializer(many=False, read_only=True, source='idProductor.idPicture')
    localizations = serializers.SlugRelatedField(many=True, slug_field='adress', read_only=True)

    class Meta:
        model = Announcement
        fields = ['email', 'username', 'idPictureProductor', 'name', 'type_of_product', 'description', 'price', 'idPicture', 'likes', 'localizations']