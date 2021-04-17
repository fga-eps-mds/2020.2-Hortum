from rest_framework.routers import SimpleRouter, Route

from ..routers import CustomUpdateRouter
from . import viewsets

routerRegister = SimpleRouter()
routerRegister.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

router = CustomUpdateRouter()
router.register(r'fav-announcement', viewsets.AddFavoritesAnnouncementsAPIView, basename='favAnnouncement')

urlpatterns = [
] + router.urls
