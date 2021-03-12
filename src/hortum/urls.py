from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('hortum.customer.urls')),
    path('productor/', include('hortum.productor.urls')),
]
