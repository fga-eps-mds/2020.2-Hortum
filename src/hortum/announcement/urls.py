from ..routers import OptionalSlashRouter
from . import viewsets
from ..routers import CustomListRouter

router = OptionalSlashRouter()
router.register(r'create', viewsets.AnnouncementRegistrationAPIView, basename='createAnnoun')
router.register(r'update', viewsets.AnnouncementDeleteUpdateAPIView, basename='deleteUpdateAnnoun')
router.register(r'retrieve/(?P<encoded_email>.+)', viewsets.AnnouncementProductorListAPIView, basename='retrieveAnnounProd')

listRouter = CustomListRouter()
listRouter.register(r'list', viewsets.AnnouncementListAPIView, basename='listAnnoun')

urlpatterns = [
] + router.urls + listRouter.urls
