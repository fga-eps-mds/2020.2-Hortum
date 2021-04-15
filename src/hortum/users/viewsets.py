from . import serializer

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User

from .serializer import ChangePasswordSerializer, UpdateUserSerializer

from rest_framework import permissions, generics, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(["GET", "PUT"])
@permission_classes([permissions.IsAuthenticated, ])
def is_token_valid(request):
    '''
    EndPoint para checagem do token
    '''
    user = User.objects.get(email=request.user)
    return Response({
        'user': user.username,
        'is_productor': user.is_productor
    })

class CustomTokenObtainPairView(TokenObtainPairView):
    '''
    EndPoint sobrescrito para obtenção do token
    '''
    serializer_class = serializer.CustomTokenObtainPairSerializer

class ChangePasswordView(GenericViewSet, mixins.UpdateModelMixin):
    """
    EndPoint para trocar a senha
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'username'

    def get_object(self):
        return User.objects.get(email=self.request.user)

    def get_serializer_context(self):
        context = super(ChangePasswordView, self).get_serializer_context()
        context.update({'user': self.get_object()})
        return context

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.set_password(serializer.data.get('new_password'))
        instance.save()

        return Response('Senha alterada com sucesso!', status=200)

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self, queryset=None):
        user = self.request.user
        return user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.email == serializer.data.get("email"):
                if self.queryset.filter(email=serializer.data.get("email")).exists():
                    return Response('Email ja registrado!', status=401)
                self.object.email = serializer.data.get("email")
            
            self.object.username = serializer.data.get("username")
            self.object.save()

            return Response('Dados alterados!', status=200)
            
        return Response('Campos vazios', status=400)