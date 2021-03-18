from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('signup/', include('hortum.users.urls')),
]
