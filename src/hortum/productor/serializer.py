from rest_framework import serializers
from .models import Productor, Localization

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields = ['name', 'email', 'password', 'idPicture', 'idAnun']

class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ['adress']