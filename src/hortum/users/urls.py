from django.urls import path, include

from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'confirm', viewsets.UserListRetrieveAPIView, basename='user')

urlpatterns = [
    path('customer/', include('hortum.customer.urls')),
    path('productor/', include('hortum.productor.urls')),
] + router.urls
