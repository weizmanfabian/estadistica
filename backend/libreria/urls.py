from os import stat
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crearLibro, name='crear'),
    path('libros/editar', views.editarLibro, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
