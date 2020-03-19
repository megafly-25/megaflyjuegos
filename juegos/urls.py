from django.urls import path
from django.conf.urls import handler404
from .views import mi_error_404, principal, juego,categoria,anio,requisitos

urlpatterns = [
    path('',principal,name="principal"),
    path('juegos/<slug>',juego,name="juego"),
    path('categoria/<slug>',categoria,name="categoria"),
    path('juegos-por-año/<anio_estreno>',anio,name="anio"),
    path('juegos-por-recursos/<requisitos>',requisitos,name="requisitos"),
    #path('sitemap.xlm',sitemap),


]
handler404=mi_error_404
#