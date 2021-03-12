from .serializer import ProductorSerializer

from .models import Productor
from ..users.models import User

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions

class ProductorRegistrationAPIView(CreateAPIView):
	'''
	EndPoint para registro de produtor
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductorSerializer
	queryset = Productor.objects.all()

class ProductorRetriveAPIView(RetrieveAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductorSerializer
	queryset = Productor.objects.all()
