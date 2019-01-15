from django.urls import path
from django.conf.urls import url,include
from .views import  PersonaFormulario,login_form,signup_view,datos,logout_func,upload_Docs

app_name='usuarios'
urlpatterns = [
    #url(r"$", index),
    path(r"datos/", datos, name="datos"),
    path(r"login/", login_form, name="login"),
    path(r"signup/", signup_view, name="signup"),
    path(r'logout/',logout_func, name='logout'),
    path(r"uploadDocs/", upload_Docs, name="Docs")
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
]
