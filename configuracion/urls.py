from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic.base import RedirectView # <--- Importante para Google

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
    
    # Redirecciones para que Google encuentre tus archivos en /static/
    path('robots.txt', RedirectView.as_view(url='/static/robots.txt')),
    path('sitemap.xml', RedirectView.as_view(url='/static/sitemap.xml')),
]

# Esto permite que las fotos se sirvan (Configuración para Render)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]