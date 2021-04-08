from rest_framework import routers

from . import viewsets

routerRegister = routers.SimpleRouter()
routerRegister.register(r'', viewsets.ProductorRegistrationAPIView, basename='productor')

router = routers.SimpleRouter()
router.register(r'list', viewsets.ProductorListAPIView, basename='listProductors')
slashless_router = routers.DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
] + slashless_router.urls + router.urls
