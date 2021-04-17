from . import serializer
from ..announcement.serializer import AnnouncementListSerializer

from .models import Customer
from ..announcement.models import Announcement
from ..productor.models import Productor

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

class CustomerRegistrationAPIView (GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
	'''
	EndPoint para registro de User's
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = serializer.CustomerSerializer
	queryset = Customer.objects.all()

class CustomerListFavoritesAPIView (GenericViewSet, mixins.RetrieveModelMixin):
	'''
	EndPoint para listagem dos favoritos
	'''
	permission_classes = (permissions.IsAuthenticated,)
	lookup_field = 'favorites'

	def get_object(self):
		return Customer.objects.get(user__email=self.request.user)

	def get_serializer_class(self):
		favorites = self.kwargs['favorites']
		if favorites == 'announcements':
			return serializer.CustomerFavoritesAnnouncementsSerializer
		elif favorites == 'productors':
			return serializer.CustomerFavoritesProductorsSerializer
		raise ParseError({'Favorites': 'Atributo inválido!'})


class FavoritesAnnouncementsAPIView (GenericViewSet, mixins.UpdateModelMixin):
	'''
	EndPoint para adição/remoção de anúncios da lista de favoritos
	'''
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = serializer.CustomerAddAnnouncementSerializer

	def get_object(self):
		return Customer.objects.get(user__email=self.request.user)

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		anun = Announcement.objects.get(idProductor=Productor.objects.get(user__email=serializer.data.get('email')), name=serializer.data.get('announcementName'))
		instance.idAnunFav.remove(anun) if instance.idAnunFav.filter(pk=anun.pk).exists() else instance.idAnunFav.add(anun)

		return Response('Annúncio atualizado com sucesso', status=200)