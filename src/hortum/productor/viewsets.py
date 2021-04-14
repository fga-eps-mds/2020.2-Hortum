from .serializer import ProductorSerializer, ProductorListSerializer

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
	EndPoint para listagem de produtores pelo nome em ordem alfabética
	'''
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = ProductorListSerializer
	queryset = Productor.objects.all()

	def get_queryset(self):
		if 'productorName' in self.kwargs:
			return Productor.objects.filter(user__username__icontains=self.kwargs['productorName']).order_by('user__username')
		else:
			return Productor.objects.order_by('user__username')
