from . import serializer

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User
from .permissions import IsProductor, IsOwnerAnnouncement

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.exceptions import ParseError

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
	EndPoint para listagem de anúncios em ordem crescente de nome
	'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementListSerializer
	
    def get_queryset(self):
        queryset = Announcement.objects.filter(inventory=True)
        if self.kwargs:
            queryset = queryset.filter(name__icontains=self.kwargs['announcementName'])
        return queryset

class AnnouncementProductorListAPIView(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementListSerializer
	
    def get_queryset(self):
        email = decode_string(self.kwargs['encoded_email'])
        if not Productor.objects.filter(user__email=email).exists():
            raise ParseError({'ProductorEmail': 'Email inexistente de produtor'})
        query = Announcement.objects.filter(idProductor__user__email=email)
        return query if email == self.request.user.get_username() else query.filter(inventory=True)