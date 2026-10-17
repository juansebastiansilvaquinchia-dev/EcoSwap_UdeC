from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.iniciar_sesion, name="iniciar_sesion"),
    path("perfil/", views.perfil_usuario, name="perfil_usuario"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
]