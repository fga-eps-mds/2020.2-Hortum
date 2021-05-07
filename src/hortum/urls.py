from .users import viewsets
from .users.urls import signup_urls

from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Hortum API",
      default_version='v0.5.5',
      description="API do aplicativo Hortum",
      terms_of_service="https://fga-eps-mds.github.io/2020.2-Hortum/CONTRIBUTING/",
      contact=openapi.Contact(email="mdsgrupo6@gmail.com"),
      license=openapi.License(name="GPLv3 License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('login/', viewsets.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/test_token/', viewsets.is_token_valid, name='is_token_valid'),
    path('admin/', admin.site.urls),
    path('signup/', include(signup_urls)),
    path('announcement/', include('hortum.announcement.urls')),
    path('productor/', include('hortum.productor.urls')),
    path('customer/', include('hortum.customer.urls')),
    path('users/', include('hortum.users.urls')),
    path('complaint/', include('hortum.complaint.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
