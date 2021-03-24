from django.contrib import admin
from django.urls import path, include
from hortum.users import viewsets

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', viewsets.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('signup/', include('hortum.users.urls')),
    path('announcement/', include('hortum.announcement.urls')),
    path('productor/', include('hortum.productor.urls')),
]
