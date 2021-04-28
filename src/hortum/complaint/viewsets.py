from .serializer import ComplaintListSerializer, ComplaintCreateSerializer, ComplaintDeleteSerializer

from .models import Complaint
from ..productor.models import Productor

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from ..encode import decode_string

class ComplaintRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    '''
    EndPoint para registro de reclamação
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ComplaintCreateSerializer
    queryset = Complaint.objects.all()

    def get_serializer_context(self):
        context = super(ComplaintRegistrationAPIView, self).get_serializer_context()
        context.update({'customer': self.request.user})
        return context

class ComplaintListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
    EndPoint para listagem de reclamações
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ComplaintListSerializer
    
    def get_queryset(self):
        emailProductor = decode_string(self.kwargs['emailProductor'])
        if not Productor.objects.filter(user__email=emailProductor).exists():
            raise ParseError({'emailProductor': 'Email inexistente de produtor'})
        queryset = Complaint.objects.filter(idProductor__user__email=emailProductor)
        return queryset.order_by('author')

class ComplaintDeleteAPIView(GenericViewSet, mixins.DestroyModelMixin):
    '''
    EndPoint para remoção de reclamação
    '''
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ComplaintDeleteSerializer
    lookup_field = 'emailCustomer'

    def get_queryset(self):
        emailCustomer = decode_string(self.kwargs['emailCustomer'])
        queryset = Complaint.objects.filter(emailCustomer=emailCustomer)
        return queryset

    def get_serializer_context(self):
        context = super(ComplaintDeleteAPIView, self).get_serializer_context()
        context.update({'queryset': self.get_queryset()})
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance.filter(idProductor__user__email=request.data['emailProductor']))
        return Response('Deletado com sucesso')
