from django.urls import path

from rest_framework import routers

from . import viewsets

routerRegister = routers.SimpleRouter()
routerRegister.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

urlpatterns = [
]
