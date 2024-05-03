from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from setup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')),
    path('', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
