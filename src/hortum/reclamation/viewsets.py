from .serializer import ReclamationListSerializer, ReclamationCreateSerializer

from .models import Reclamation
from ..productor.models import Productor
from ..customer.models import Customer
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from django.shortcuts import get_object_or_404

from ..encode import decode_string

class ReclamationRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    '''
    EndPoint para registro de reclamação
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReclamationCreateSerializer
    queryset = Reclamation.objects.all()

    def get_serializer_context(self):
        context = super(ReclamationRegistrationAPIView, self).get_serializer_context()
        context.update({'customer': self.request.user})
        return context

class ReclamationListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
    EndPoint para listagem de reclamações
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReclamationListSerializer
    queryset = Reclamation.objects.all()
    
    def get_queryset(self):
        emailProductor = decode_string(self.kwargs['emailProductor'])
        queryset = self.queryset.filter(idProductor=Productor.objects.get(user__email=emailProductor))
        return queryset.order_by('author')
