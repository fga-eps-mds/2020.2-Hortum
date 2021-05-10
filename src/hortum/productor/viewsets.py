from .serializer import ProductorSerializer, ProductorListSerializer

from .models import Productor
from ..users.models import User

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

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		if response.status_code == 201:
			email = self.request.data['user']['email'] if request.content_type == 'application/json' else self.request.data['user.email']
			User.send_verification_email(request, email)
		return response

class ProductorListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
	EndPoint para listagem de produtores pelo nome em ordem alfabética
	'''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductorListSerializer

    def get_queryset(self):
        queryset = Productor.objects.all()
        if 'productorName' in self.kwargs:
            queryset = queryset.filter(user__username__icontains=self.kwargs['productorName'])
        return queryset.order_by('user__username')
