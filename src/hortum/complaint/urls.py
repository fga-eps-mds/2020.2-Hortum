from ..routers import OptionalSlashRouter
from . import viewsets

router = OptionalSlashRouter()
router.register(r'create', viewsets.ComplaintRegistrationAPIView, basename='createComplaint')
router.register(r'delete', viewsets.ComplaintDeleteAPIView, basename='deleteComplaint')
router.register(r'list(:?/(?P<emailProductor>.+))?', viewsets.ComplaintListAPIView, basename='listComplaint')

urlpatterns = [
] + router.urls
