from rest_framework import routers

from . import viewsets
from ..routers import CustomListRouter

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'create', viewsets.AnnouncementRegistrationAPIView, basename='createAnnoun')
router.register(r'update', viewsets.AnnouncementDeleteUpdateAPIView, basename='deleteUpdateAnnoun')
router.register(r'retrieve/(?P<encoded_email>.+)', viewsets.AnnouncementProductorListAPIView, basename='retrieveAnnounProd')
router.register(r'category/(?P<type_of_product>.+)', viewsets.AnnouncementListCategoryView, basename='ListAnnouCategory')

listRouter = CustomListRouter()
listRouter.register(r'list', viewsets.AnnouncementListAPIView, basename='listAnnoun')

urlpatterns = [
] + router.urls + listRouter.urls
