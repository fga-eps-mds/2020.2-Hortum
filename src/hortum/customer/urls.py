from rest_framework.routers import SimpleRouter, Route

from ..routers import CustomUpdateRouter
from . import viewsets

routerRegister = SimpleRouter()
routerRegister.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

router = CustomUpdateRouter()
router.register(r'fav-announcement', viewsets.FavoritesAnnouncementsAPIView, basename='favAnnouncement')

listRouter = SimpleRouter()
listRouter.register(r'favorites', viewsets.CustomerListFavoritesAPIView, basename='listFavAnnouncements')

urlpatterns = [
] + router.urls + listRouter.urls
