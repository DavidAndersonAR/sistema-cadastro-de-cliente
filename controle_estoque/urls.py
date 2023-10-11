"""
URL configuration for controle_estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from sistema_web import views
from clientes.views import cadastro_de_clientes, tela_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_produtos, name="cadastro_produtos"),
    path('login/',views.login_user, name="login"),
    path('cadastro_user/', views.cadastro, name="cadastro_user"),
    path('', views.usuario, name="usuario"),
    path('index/', views.index, name="index"),

    path('tela_inicio/', tela_inicio, name="tela_inicio"),

    path('tela_inicio/', cadastro_de_clientes, name="cadastro_de_clientes"),


]

