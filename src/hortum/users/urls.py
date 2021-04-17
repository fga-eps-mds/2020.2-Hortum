from django.urls import path, include

from rest_framework.routers import SimpleRouter, Route

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
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


router = CustomUpdateUserRouter()
router.register(r'change-password', viewsets.ChangePasswordView, basename='changePasswordUser')
router.register(r'update', viewsets.UpdateUserView, basename='updateUser')

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
] + router.urls
