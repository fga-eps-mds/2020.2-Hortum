from django.urls import path, include

urlpatterns = [
    path('customer/', include('hortum.customer.urls')),
    path('productor/', include('hortum.productor.urls')),
]
