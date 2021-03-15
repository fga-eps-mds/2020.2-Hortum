from django.urls import path

from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

urlpatterns = [
] + router.urls
