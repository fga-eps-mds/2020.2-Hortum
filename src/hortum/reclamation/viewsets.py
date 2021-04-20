from . import serializer

from .models import Reclamation
from ..productor.models import Productor
from ..customer.models import Customer
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions

class ReclamationRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    '''
    EndPoint para registro de reclamação
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.ReclamationCreateSerializer
    queryset = Reclamation.objects.all()

    def get_serializer_context(self):
        context = super(ReclamationRegistrationAPIView, self).get_serializer_context()
        context.update({'customer': self.request.user})
        return context