"""
URL configuration for mesa_sismica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from hola_mesa import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.hola),
    path('dato/', views.dato_view, name="dato"),
    path('iniciar_mesa/', views.hola_mesa),
    path('iniciar_mesa/mover_mesa/', views.mover_mesa, name="mover_mesa"),
    path('iniciar_mesa/reproducir_sismo/', views.reproducir_sismo, name="reproducir_sismo"),
    path('iniciar_mesa/crear_sismo/', views.crear_sismo, name="crear_sismo"),
    path('iniciar_mesa/documentacion/', views.documentacion),
    
]
