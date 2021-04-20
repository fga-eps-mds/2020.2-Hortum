from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'create', viewsets.ReclamationRegistrationAPIView, basename='createReclamation')
router.register(r'delete', viewsets.ReclamationRegistrationAPIView, basename='updateReclamation')
router.register(r'list', viewsets.ReclamationRegistrationAPIView, basename='listReclamation')

urlpatterns = [
] + router.urls
