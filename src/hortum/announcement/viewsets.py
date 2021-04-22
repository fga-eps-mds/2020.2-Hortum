from . import serializer

from .models import Announcement
from ..productor.models import Productor
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.exceptions import ParseError

from ..encode import decode_string

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
