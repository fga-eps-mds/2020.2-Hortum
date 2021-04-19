from rest_framework import routers

from . import viewsets
from ..announcement.viewsets import ProductorRetrieveAPIView

routerRegister = routers.SimpleRouter()
routerRegister.register(r'', viewsets.ProductorRegistrationAPIView, basename='productor')

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'retrieve/(?P<encoded_email>.+)', ProductorRetrieveAPIView, basename='retrieveProductor')
router.register(r'list(:?/(?P<productorName>.+))?', viewsets.ProductorListAPIView, basename='searchProductor')

urlpatterns = [
] + router.urls
