from django.urls import path
from django.conf.urls import handler404
from .views import mi_error_404, principal, juego,categoria

urlpatterns = [
    path('',principal,name="principal"),
    path('juego/<slug>',juego,name="juego"),
    path('categoria/<slug>',categoria,name="categoria")
    #path('sitemap.xlm',sitemap),


]
handler404=mi_error_404
#