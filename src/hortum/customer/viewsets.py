from . import serializer
from .models import Customer

from ..announcement.models import Announcement
from ..productor.models import Productor
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from django.db.models import F

class CustomerRegistrationAPIView (GenericViewSet, mixins.CreateModelMixin):
    '''
    EndPoint para registro de User's
    '''
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializer.CustomerSerializer
    queryset = Customer.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            email = self.request.data['user']['email']
            User.send_verification_email(request, email)
        return response

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
        anun = Announcement.objects.get(idProductor__user__email=serializer.data.get('email'), name=serializer.data.get('announcementName'))
        if instance.idAnunFav.filter(pk=anun.pk).exists():
            instance.idAnunFav.remove(anun)
            anun.likes = F('likes') - 1 if F('likes') != 0 else 0
        else:
            instance.idAnunFav.add(anun)
            anun.likes = F('likes') + 1

        anun.save()
        return Response('Anúncio atualizado com sucesso')

class FavoriteProductorsAPIView(GenericViewSet, mixins.UpdateModelMixin):
    '''
	EndPoint para adição/remoção de produtores na lista de favoritos
	'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.CustomerAddProductorSerializer

    def get_object(self):
        return Customer.objects.get(user__email=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        productor = Productor.objects.get(user__email=serializer.data.get('email'))
	
        if instance.idProdFav.filter(pk=productor.pk).exists():
            instance.idProdFav.remove(productor)
        else:
            instance.idProdFav.add(productor)

        productor.save()
        return Response('Produtores favoritos atualizados com sucesso')