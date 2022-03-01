"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core.category.views.views import *
from core.login.views import LoginFormView
from core.usuarios.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoria/', include('core.category.urls')),
    path('usuarios/', include('core.products.urls')),
    path('login/', include('core.login.urls'), name='login'),
    path('ingreso/', include('core.ingreso.urls'), name='ingreso'),
    path('pages/', include('core.paginas.urls'), name='pages'),


    #REGISTRO
    path('registro/', registro, name='registro'),
    #path('login/', login, name='login'),


    


]
