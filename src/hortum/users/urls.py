from django.urls import path, include

from ..productor.urls import routerRegister as productorRegister
from ..customer.urls import routerRegister as customerRegister

urlpatterns = [
    path('customer/', include(customerRegister.urls)),
    path('productor/', include(productorRegister.urls)),
]
