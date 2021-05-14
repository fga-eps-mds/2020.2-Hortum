from rest_framework import serializers

from django.db.models import Q

from .models import Announcement, AnnouncementImage, Localization
from ..productor.models import Productor
from ..validators import UniqueValidator

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(required=False, child=serializers.CharField(allow_blank=True), write_only=True, max_length=3)
    images = serializers.ListField(required=False, child=serializers.ImageField(), write_only=True, max_length=5)

    class Meta:
        model = Announcement
        fields = ['name', 'images', 'type_of_product', 'description', 'price', 'inventory', 'localizations', 'likes']
        extra_kwargs = {
            'name': {'validators': [UniqueValidator()]},
            'inventory': {'required': False, 'default': True}
        }

    def create(self, validated_data):
        localizations = images = []
        if 'localizations' in validated_data:
            localizations = validated_data.pop('localizations')
        if 'images' in validated_data:
            images = validated_data.pop('images')
        produtor_pk = Productor.objects.get(user__email=self.context['request'].user)
        announcement = Announcement.objects.create(idProductor=produtor_pk, **validated_data)
        [AnnouncementImage.objects.create(idImage=announcement, picture=picture) for picture in images]
        [Localization.objects.create(idAnnoun=announcement, adress=local) for local in localizations]
        return announcement

class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    localizations = serializers.ListField(child=serializers.CharField(), write_only=True, max_length=3)
    images = serializers.ListField(child=serializers.ImageField(), allow_empty=True, write_only=True, max_length=5)

    class Meta:
        model = Announcement
        fields = ['name', 'type_of_product', 'description', 'price', 'inventory', 'localizations', 'images']
        extra_kwargs = {'name': {'validators': [UniqueValidator()]}}

    def multiple_update(self, instance, validated_data, field_name, filter_obj, **query):
        query_items = list(query.items())
        data = query_items[1][1]
        filter_obj.objects.filter(Q(query_items[0]) & ~Q(query_items[1])).delete()
        for value in data:
            if not instance.__class__.objects.filter(name=instance.name, **{'%s__%s' % (field_name, query_items[1][0]): value}).exists():
                query[query_items[1][0]] = value
                filter_obj.objects.create(**query)
        instance.save()

    def update(self, instance, validated_data):
        if 'localizations' in validated_data:
            self.multiple_update(instance, validated_data, 'localizations', Localization, **{'idAnnoun': instance, 'adress': validated_data.pop('localizations')})
        if 'images' in validated_data:
            self.multiple_update(instance, validated_data, 'images', AnnouncementImage, **{'idImage': instance, 'picture': validated_data.pop('images')})
        return super().update(instance, validated_data)

class AnnouncementImageSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        return '%s://%s%s' % ('https' if self.context['request'].is_secure() else 'http', self.context['request'].get_host(), value.picture.url)

class AnnouncementListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, source='idProductor.user.username')
    email = serializers.EmailField(required=True, source='idProductor.user.email')
    localizations = serializers.SlugRelatedField(many=True, slug_field='adress', read_only=True)
    phone_number = serializers.CharField(required=True, source='idProductor.user.phone_number')
    pictureProductor = serializers.ImageField(required=True, source='idProductor.user.profile_picture')
    images = AnnouncementImageSerializer(many=True)
    
    class Meta:
        model = Announcement
        fields = ['email', 'username', 'phone_number', 'pictureProductor', 'name', 'images', 'type_of_product', 'description', 'price', 'localizations', 'likes', 'inventory']