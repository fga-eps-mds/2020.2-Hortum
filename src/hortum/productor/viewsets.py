from .serializer import ProductorSerializer, ProductorListSerializer, ProductorRetrieveSerializer

from .models import Productor
from ..users.models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from ..encode import decode_string, encode_string

class ProductorRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
	'''
	EndPoint para registro de produtor
	'''
	permission_classes = (permissions.AllowAny,)
	serializer_class = ProductorSerializer
	queryset = Productor.objects.all()

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		if response.status_code == 201:
			email = self.request.data['user']['email']
			User.send_verification_email(email)
		return response

class ProductorRetrieveAPIView(GenericViewSet, mixins.RetrieveModelMixin):
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = ProductorRetrieveSerializer
	queryset = Productor.objects.all()
	lookup_field = 'encoded_email'
	
	def get_object(self):
		email = decode_string(self.kwargs['encoded_email'])
		prod = get_object_or_404(self.queryset.filter(user__email=email))
		return prod

class ProductorListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
	EndPoint para listagem de produtores pelo nome em ordem alfabética
	'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductorListSerializer
    queryset = Productor.objects.all()

    def get_queryset(self):
        query = Productor.objects.all()
        if 'productorName' in self.kwargs:
            query = query.filter(user__username__icontains=self.kwargs['productorName'])
        return query.order_by('user__username')
