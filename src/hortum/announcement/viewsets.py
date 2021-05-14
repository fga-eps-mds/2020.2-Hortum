from . import serializer

from .models import Announcement

from ..customer.models import Customer
from ..productor.models import Productor
from ..productor.permissions import IsProductor, IsOwnerAnnouncement

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.exceptions import ParseError, NotFound

from ..encode import decode_string

class AnnouncementRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    '''
	EndPoint para registro de anúncios
	'''
    permission_classes = (permissions.IsAuthenticated, IsProductor,)
    serializer_class = serializer.AnnouncementCreateSerializer

    def get_queryset(self):
        return Productor.objects.get(user__email=self.request.user).announcements.all()

class AnnouncementDeleteUpdateAPIView(GenericViewSet, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    '''
	EndPoint para atualização/remoção de anúncios
	'''
    permission_classes = (permissions.IsAuthenticated, IsProductor, IsOwnerAnnouncement)
    serializer_class = serializer.AnnouncementUpdateSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return Productor.objects.get(user__email=self.request.user).announcements.all()

class AnnouncementListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
	EndPoint para listagem de anúncios de acordo com o filtro e o valor passados
	'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementListSerializer
	
    def get_queryset(self):
        queryset = Announcement.objects.filter(inventory=True)
        query_params = self.request.GET
        possible_filters = ['name', 'localizations__adress', 'type_of_product']
        if Customer.objects.filter(user__email=self.request.user).exists():
            queryset = queryset.exclude(customer__user__email=self.request.user)
        if len(query_params) == 0:
            return queryset
        if 'filter' and 'value' not in query_params or len(query_params) != 2:
            raise NotFound({'query_params': 'Parametros passados para a query incoerentes'})
        if query_params.get('filter') in possible_filters:
            return queryset.filter(**{'%s__icontains' % (query_params.get('filter')): query_params.get('value')}).distinct()
        raise ParseError({'filter': 'Campo para filtragem inexistente'})

class AnnouncementProductorListAPIView(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementListSerializer
	
    def get_queryset(self):
        email = decode_string(self.kwargs['encoded_email'])
        if not Productor.objects.filter(user__email=email).exists():
            raise ParseError({'ProductorEmail': 'Email inexistente de produtor'})
        query = Announcement.objects.filter(idProductor__user__email=email)
        return query if email == self.request.user.get_username() else query.filter(inventory=True)