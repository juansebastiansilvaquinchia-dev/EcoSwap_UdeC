from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketplace.urls')), # conectamos las rutas del catalogo a la ruta raiz del proyecto
    path('usuarios/', include('usuarios.urls')),
]

# configuracion para servir archivos multimedia (images de productos) durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)