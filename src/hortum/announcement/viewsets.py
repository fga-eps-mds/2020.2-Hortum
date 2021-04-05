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
    queryset = Announcement.objects.all()

class AnnouncementDeleteUpdateAPIView(GenericViewSet, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    '''
    EndPoint para remoção de anúncio
    '''
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Productor.objects.all()
    serializer_class = serializer.AnnouncementUpdateSerializer
    lookup_field = 'name'

    def get_queryset(self):
        productor = Productor.objects.get(user=User.objects.get(email=self.request.user))
        return productor.announcements.all()
