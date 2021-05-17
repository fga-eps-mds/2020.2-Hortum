from rest_framework import serializers

from .models import Complaint
from ..productor.models import Productor
from ..validators import ExistingValidator, UniqueValidator

class ComplaintSerializer(serializers.ModelSerializer):
    emailProductor = serializers.EmailField(required=True, source='idProductor.user.email', write_only=True, validators=[UniqueValidator()])

    class Meta:
        model = Complaint
        fields = ['author', 'description', 'emailProductor', 'image']

    def create(self, validated_data):
        productor_pk = Productor.objects.get(user__email=validated_data.pop('idProductor')['user']['email'])
        complaint = Complaint.objects.create(idProductor=productor_pk, **validated_data, emailCustomer=self.context['request'].user)
        return complaint

class ComplaintDeleteSerializer(serializers.ModelSerializer):
    emailProductor = serializers.EmailField(required=True, source='idProductor.user.email', write_only=True, validators=[ExistingValidator()])

    class Meta:
        model = Complaint
        fields = ['emailProductor']