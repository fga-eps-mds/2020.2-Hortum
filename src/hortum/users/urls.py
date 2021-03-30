from django.urls import path, include

from rest_framework import routers
from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'confirm', viewsets.UserListRetrieveAPIView, basename='user')

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
] + router.urls
