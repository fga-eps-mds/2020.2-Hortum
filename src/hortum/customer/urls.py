from rest_framework.routers import SimpleRouter

from ..routers import CustomUpdateRouter, OptionalSlashRouter
from . import viewsets

routerRegister = SimpleRouter()
routerRegister.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

router = CustomUpdateRouter()
router.register(r'fav-announcement', viewsets.FavoritesAnnouncementsAPIView, basename='favAnnouncement')
router.register(r'fav-productor', viewsets.FavoriteProductorsAPIView, basename='favProductor')

listRouter = OptionalSlashRouter()
listRouter.register(r'favorites', viewsets.CustomerListFavoritesAPIView, basename='listFavAnnouncements')

urlpatterns = [
] + router.urls + listRouter.urls
