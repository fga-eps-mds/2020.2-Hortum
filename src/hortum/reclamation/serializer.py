from rest_framework import serializers

from .models import Reclamation
from ..productor.models import Productor

from ..picture.serializer import PictureSerializer

class ReclamationCreateSerializer(serializers.ModelSerializer):
    idPicture = PictureSerializer(read_only=True)
    emailProductor = serializers.EmailField(required=True, write_only=True)

    class Meta:
        model = Reclamation
        fields = ['author', 'description', 'emailProductor', 'idPicture']

    def validate(self, data):
        if Reclamation.objects.filter(emailCustomer=self.context['customer']).exists():
            raise serializers.ValidationError({'emailProductor': 'Consumidor já possui reclamação com este produtor.'})
        return data

    def create(self, validated_data):
        productor_pk = Productor.objects.get(user__email=validated_data.pop('emailProductor'))
        print(type(self.context['customer']))
        reclamation = Reclamation.objects.create(idProductor=productor_pk, **validated_data, emailCustomer=self.context['customer'])
        return reclamation