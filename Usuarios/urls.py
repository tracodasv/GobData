from django.urls import path
from django.conf.urls import url,include
from .views import  login_form,signup_view,logout_func,upload_Docs,PersonaUpdateView,RedirectPerfil

app_name='usuarios'
urlpatterns = [
    #url(r"$", index),
    path(r"login/", login_form, name="login"),
    path(r"signup/", signup_view, name="signup"),
    path(r'logout/',logout_func, name='logout'),
    path(r"uploadDocs/", upload_Docs, name="Docs"),
    path("miInfo/<int:pk>", PersonaUpdateView.as_view(), name="perfil"),
    path("miInfo", RedirectPerfil.as_view(), name="uperfil"),
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
]
