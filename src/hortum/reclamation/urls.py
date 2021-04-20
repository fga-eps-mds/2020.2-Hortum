from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'create', viewsets.ReclamationRegistrationAPIView, basename='createReclamation')
router.register(r'delete', viewsets.ReclamationRegistrationAPIView, basename='updateReclamation')
router.register(r'list(:?/(?P<emailProductor>.+))?', viewsets.ReclamationListAPIView, basename='listReclamation')

urlpatterns = [
] + router.urls
