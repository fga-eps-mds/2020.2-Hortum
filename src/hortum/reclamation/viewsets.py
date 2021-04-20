from .serializer import ReclamationListSerializer, ReclamationCreateSerializer, ReclamationDeleteSerializer

from .models import Reclamation
from ..productor.models import Productor
from ..customer.models import Customer
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.response import Response

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
    
    def get_queryset(self):
        emailProductor = decode_string(self.kwargs['emailProductor'])
        queryset = Reclamation.objects.filter(idProductor=Productor.objects.get(user__email=emailProductor))
        return queryset.order_by('author')

class ReclamationDeleteAPIView(GenericViewSet, mixins.DestroyModelMixin):
    '''
    EndPoint para remoção de reclamação
    '''
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ReclamationDeleteSerializer
    lookup_field = 'emailCustomer'

    def get_queryset(self):
        emailCustomer = decode_string(self.kwargs['emailCustomer'])
        queryset = Reclamation.objects.filter(emailCustomer=emailCustomer)
        return queryset

    def get_serializer_context(self):
        context = super(ReclamationDeleteAPIView, self).get_serializer_context()
        context.update({'queryset': self.get_queryset()})
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance.filter(idProductor__user__email=request.data['emailProductor']))
        return Response('Deletado com sucesso')

