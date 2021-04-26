from rest_framework import routers

from . import viewsets

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'create', viewsets.ComplaintRegistrationAPIView, basename='createComplaint')
router.register(r'delete', viewsets.ComplaintDeleteAPIView, basename='deleteComplaint')
router.register(r'list(:?/(?P<emailProductor>.+))?', viewsets.ComplaintListAPIView, basename='listComplaint')

urlpatterns = [
] + router.urls
