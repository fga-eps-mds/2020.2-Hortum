from . import serializer

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User

from .serializer import ChangePasswordSerializer, UpdateUserSerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, generics
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

class UserListRetrieveAPIView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.UserSerializer
    queryset = User.objects.all()

class CustomTokenObtainPairView(TokenObtainPairView):
    '''
    EndPoint sobrescrito para obtenção do token
    '''
    serializer_class = serializer.CustomTokenObtainPairSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint para alterar a senha
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response("Senha incorreta!")
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = 'Senha alterada!'


            return Response(response)

        return Response(serializer.errors)

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
                    return Response("Email ja registrado!")
                self.object.email = serializer.data.get("email")
            
            self.object.username = serializer.data.get("username")
            self.object.save()
            response = 'Dados alterados!'

            return Response(response)
            
        return Response(serializer.errors)