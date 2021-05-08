from django.urls import path, include
from rest_framework import routers

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
from ..routers import CustomUpdateRouter, CustomDeleteRouter, OptionalSlashRouter
from . import viewsets

router = CustomUpdateRouter()
router.register(r'change-password', viewsets.ChangePasswordView, basename='changePasswordUser')
router.register(r'update', viewsets.UpdateUserView, basename='updateUser')

customRouter = CustomDeleteRouter()
customRouter.register(r'delete', viewsets.UserDeleteAPIView, basename='deleteUser')

routerVerify = OptionalSlashRouter()
routerVerify.register(r'verify', viewsets.VerifyAccountView, basename='verifyEmail')

urlpatterns = router.urls + routerVerify.urls + customRouter.urls

signup_urls = [
    path('customer', include(customerRegister.urls)),
    path('productor', include(productorRegister.urls)),
]