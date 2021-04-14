from django.urls import path, include

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister
from . import viewsets

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
    path('change-password/', viewsets.ChangePasswordView.as_view(), name='change-password'),
    path('update/', viewsets.UpdateUserView.as_view(), name='update-user'),
]
