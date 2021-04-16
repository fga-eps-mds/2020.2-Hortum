from rest_framework.routers import SimpleRouter, Route

from . import viewsets

class CustomUpdateUserRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/?$',
            mapping={'patch': 'update'},
            name='{basename}-update',
            detail=False,
            initkwargs={}
        )
    ]

routerRegister = SimpleRouter()
routerRegister.register(r'', viewsets.CustomerRegistrationAPIView, basename='customer')

router = CustomUpdateUserRouter()
router.register(r'fav-announcement', viewsets.AddFavoritesAnnouncementsAPIView, basename='favAnnouncement')

urlpatterns = [
] + router.urls
