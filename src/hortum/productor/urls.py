from rest_framework.routers import SimpleRouter

from ..routers import OptionalSlashRouter
from . import viewsets

routerRegister = SimpleRouter()
routerRegister.register(r'', viewsets.ProductorRegistrationAPIView, basename='productor')

router = OptionalSlashRouter()
router.register(r'list(:?/(?P<productorName>.+))?', viewsets.ProductorListAPIView, basename='searchProductor')

urlpatterns = [
] + router.urls