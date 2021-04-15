from django.urls import path, include

from rest_framework import routers

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'change-password', viewsets.ChangePasswordView, basename='changePasswordUser')

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
    path('update/', viewsets.UpdateUserView.as_view(), name='update-user'),
] + router.urls
