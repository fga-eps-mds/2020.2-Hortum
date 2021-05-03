from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from . import serializer

from .serializer import ChangePasswordSerializer, UpdateUserSerializer
from .permissions import IsVerified

from rest_framework import permissions, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render

from ..encode import decode_string

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

class VerifyAccountView(GenericViewSet, mixins.RetrieveModelMixin):
    '''
    EndPoint para confirmação de email da conta
    '''
    serializer_class = serializer.UserSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'encoded_email'

    def get_object(self):
        email = decode_string(self.kwargs['encoded_email'])
        return User.objects.get(email=email)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_verified:
            return render(request, 'hortum/user_already_verified_page.html', status=400)
            
        instance.is_verified = True
        instance.save()
        return render(request, 'hortum/user_verify_page.html')
        
class CustomTokenObtainPairView(TokenObtainPairView):
    '''
    EndPoint sobrescrito para obtenção do token
    '''
    serializer_class = serializer.CustomTokenObtainPairSerializer
    permission_classes = (IsVerified,)

class UserDeleteAPIView(GenericViewSet, mixins.DestroyModelMixin):
    '''
    EndPoint para deleção de usuários
    '''
    serializer_class = serializer.UserDeleteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return User.objects.get(email=self.request.user)

    def get_serializer_context(self):
        context = super(UserDeleteAPIView, self).get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordView(GenericViewSet, mixins.UpdateModelMixin):
    """
    EndPoint para trocar a senha
    """
    serializer_class = serializer.ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

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

class UpdateUserView(GenericViewSet, mixins.UpdateModelMixin):
    '''
    EndPoint para trocar username e email
    '''
    serializer_class = serializer.UpdateUserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(email=self.request.user)

    def get_serializer_context(self):
        context = super(UpdateUserView, self).get_serializer_context()
        context.update({'user': self.get_object(), 'queryset': self.get_queryset()})
        return context
