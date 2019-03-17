"""PulpApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from Solicitudes.views import home_view
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
    url("usuarios/",include('Usuarios.urls',namespace="usuarios")),
    url("solicitudes/",include('Solicitudes.urls',namespace='solicitudes') ),
    url("alcaldias/",include('Alcaldias.urls',namespace='alcaldias')),
    path("", home_view, name="home"),
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),
    path("creditos/", TemplateView.as_view(template_name='creditos.html'), name="creditos"),
]
