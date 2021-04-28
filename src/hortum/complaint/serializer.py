from rest_framework import serializers

from .models import Complaint
from ..productor.models import Productor

class ComplaintCreateSerializer(serializers.ModelSerializer):
    emailProductor = serializers.EmailField(required=True, write_only=True)

    class Meta:
        model = Complaint
        fields = ['author', 'description', 'emailProductor', 'image']

    def validate_emailProductor(self, emailProductor):
        if Complaint.objects.filter(emailCustomer=self.context['customer'], idProductor__user__email=emailProductor).exists():
            raise serializers.ValidationError('Consumidor já possui reclamação com este produtor.')
        return emailProductor

    def create(self, validated_data):
        productor_pk = Productor.objects.get(user__email=validated_data.pop('emailProductor'))
        complaint = Complaint.objects.create(idProductor=productor_pk, **validated_data, emailCustomer=self.context['customer'])
        return complaint

class ComplaintListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Complaint
        fields = ['author', 'description', 'image']

class ComplaintDeleteSerializer(serializers.ModelSerializer):
    emailProductor = serializers.EmailField(required=True, write_only=True)

    class Meta:
        model = Complaint
        fields = ['emailProductor']

    def validate_emailProductor(self, emailProductor):
        if not self.context['queryset'].filter(idProductor__user__email=emailProductor).exists():
            raise serializers.ValidationError({'emailProductor': 'Nenhuma reclamação deste customer com este productor'})
        return emailProductor