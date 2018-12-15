from django.urls import path
from django.conf.urls import url,include
from .views import index, PersonaFormulario,login_form,signup_view,datos

app_name='usuarios'
urlpatterns = [
    #url(r"$", index),
    path(r"datos/", datos, name="datos"),
    path(r"login/", login_form, name="login"),
    path(r"signup/", signup_view, name="signup")
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
]
