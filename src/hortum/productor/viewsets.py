from .serializer import ProductorSerializer

from .models import Productor

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions

class ProductorRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
	'''
	EndPoint para registro de produtor
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductorSerializer
	queryset = Productor.objects.all()

class ProductorListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
    EndPoint para listar todos produtores e anúncios
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductorSerializer
    queryset = Productor.objects.all()
