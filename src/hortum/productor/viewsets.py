from .serializer import ProductorSerializer, ProductorRetrieveSerializer

from .models import Productor

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions

from ..encode import decode_string

class ProductorRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
	'''
	EndPoint para registro de produtor
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductorSerializer
	queryset = Productor.objects.all()

class ProductorRetrieveAPIView(GenericViewSet, mixins.RetrieveModelMixin):
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = ProductorRetrieveSerializer
	queryset = Productor.objects.all()
	lookup_field = 'encoded_email'
	
	def get_object(self):
		email = decode_string(self.kwargs['encoded_email'])
		return Productor.objects.get(user__email=email)
