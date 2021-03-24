from .serializer import AnnouncementSerializer

from .models import Announcement

from rest_framework.viewsets import GenericViewSet 
from rest_framework import mixins
from rest_framework import permissions

class AnnouncementRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
	'''
	EndPoint para registro de anúncio
	'''
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = AnnouncementSerializer
	queryset = Announcement.objects.all()