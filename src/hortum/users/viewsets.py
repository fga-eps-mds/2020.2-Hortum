from .serializer import UserSerializer

from .models import User

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions

class UserListRetrieveAPIView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
