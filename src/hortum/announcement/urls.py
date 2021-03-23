from django.urls import path
from django.contrib import admin

from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'create', viewsets.AnnouncementRegistrationAPIView, basename='announcement')

urlpatterns = [
] + router.urls
