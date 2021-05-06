from django.urls import path, include
from rest_framework import routers

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
from ..routers import CustomUpdateRouter, CustomDeleteRouter
from . import viewsets

router = CustomUpdateRouter()
router.register(r'change-password', viewsets.ChangePasswordView, basename='changePasswordUser')
router.register(r'update', viewsets.UpdateUserView, basename='updateUser')

customRouter = CustomDeleteRouter()
customRouter.register(r'delete', viewsets.UserDeleteAPIView, basename='deleteUser')

routerVerify = routers.SimpleRouter(trailing_slash=True)
routerVerify.register(r'verify', viewsets.VerifyAccountView, basename='verifyEmail')

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
] + router.urls + routerVerify.urls + customRouter.urls