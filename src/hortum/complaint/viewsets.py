from .serializer import ComplaintSerializer, ComplaintDeleteSerializer

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
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()

class ComplaintListAPIView(GenericViewSet, mixins.ListModelMixin):
    '''
    EndPoint para listagem de reclamações
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ComplaintSerializer
    
    def get_queryset(self):
        emailProductor = decode_string(self.kwargs['emailProductor'])
        if not Productor.objects.filter(user__email=emailProductor).exists():
            raise ParseError({'emailProductor': 'Email inexistente de produtor'})
        return Complaint.objects.filter(idProductor__user__email=emailProductor).order_by('author')

class ComplaintDeleteAPIView(GenericViewSet, mixins.DestroyModelMixin):
    '''
    EndPoint para remoção de reclamação
    '''
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ComplaintDeleteSerializer
    lookup_field = 'emailCustomer'

    def get_queryset(self):
        emailCustomer = decode_string(self.kwargs['emailCustomer'])
        return Complaint.objects.filter(emailCustomer=emailCustomer)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance.filter(idProductor__user__email=request.data['emailProductor']))
        return Response('Deletado com sucesso')
