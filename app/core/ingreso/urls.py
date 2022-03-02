from django.urls import path, include
from core.ingreso.views import *
urlpatterns = [
    path('', LoginFormView.as_view(), name='ingreso'),
    path('logout/', LogoutView.as_view(), name='salir_Logout'),
]