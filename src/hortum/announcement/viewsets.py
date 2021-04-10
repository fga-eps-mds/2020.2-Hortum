from . import serializer

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions

class AnnouncementRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    '''
    EndPoint para registro de anúncio
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementCreateSerializer

    def get_serializer_context(self):
        context = super(AnnouncementRegistrationAPIView, self).get_serializer_context()
        context.update({'productor': Productor.objects.get(user=User.objects.get(email=self.request.user))})
        return context

class AnnouncementDeleteUpdateAPIView(GenericViewSet, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    '''
    EndPoint para remoção de anúncio
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementUpdateSerializer
    lookup_field = 'name'

    def get_queryset(self):
        productor = Productor.objects.get(user=User.objects.get(email=self.request.user))
        return productor.announcements.all()

    def get_serializer_context(self):
        context = super(AnnouncementDeleteUpdateAPIView, self).get_serializer_context()
        context.update({'queryset': self.get_queryset()})
        return context

class AnnouncementListAPIView(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.AnnouncementListSerializer
    queryset = Announcement.objects.filter(inventory=True)