from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="DCU Clubs API",
        default_version='v1',
        description="API documentation for DCU Clubs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('clubs.urls')),  # clubs/urls.py 포함
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]