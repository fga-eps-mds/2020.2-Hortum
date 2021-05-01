from django.urls import path, include

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
from ..routers import CustomUpdateRouter, CustomDeleteRouter
from . import viewsets

router = CustomUpdateRouter()
router.register(r'change-password', viewsets.ChangePasswordView, basename='changePasswordUser')
router.register(r'update', viewsets.UpdateUserView, basename='updateUser')

customRouter = CustomDeleteRouter()
customRouter.register(r'delete', viewsets.UserDeleteAPIView, basename='deleteUser')

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
] + router.urls + customRouter.urls
