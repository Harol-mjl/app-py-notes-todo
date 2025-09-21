from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    #Swagger
    path('schema/',SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #Apps
    path('api/v1/', include('apps.notes.v1.urls')),
    path('api/v1/', include('apps.users.v1.urls')),
]
