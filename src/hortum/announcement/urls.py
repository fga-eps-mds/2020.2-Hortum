from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'create', viewsets.AnnouncementRegistrationAPIView, basename='createAnnoun')
router.register(r'update', viewsets.AnnouncementDeleteUpdateAPIView, basename='deleteUpdateAnnoun')
router.register(r'list(:?/(?P<announcementName>.+))?', viewsets.AnnouncementListAPIView, basename='listAnnoun')
router.register(r'retrieve/(?P<encoded_email>.+)', viewsets.AnnouncementProductorListAPIView, basename='retrieveAnnounProd')

urlpatterns = [
] + router.urls
