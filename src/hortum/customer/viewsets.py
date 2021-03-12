from .serializer import CustomerSerializer

from .models import Customer
from ..users.models import User

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions

class CustomerRegistrationAPIView(CreateAPIView):
	'''
	EndPoint para registro de usuário
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()

class CustomerRetriveAPIView(RetrieveAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()
