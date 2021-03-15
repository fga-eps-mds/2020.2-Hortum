from .serializer import CustomerSerializer

from .models import Customer

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions

class CustomerRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
	'''
	EndPoint para registro de usuário
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
