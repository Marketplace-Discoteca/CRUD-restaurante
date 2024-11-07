from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/crear/', views.crear, name='crear'),
    path('servicios/editar/<int:id>/', views.editar, name='editar'),
    path('servicios/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('servicios/detalle/<int:id>/', views.detalle, name='detalle'),  # Nueva URL para detalle
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
