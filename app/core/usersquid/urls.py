from django.urls import path
from core.usersquid.views.views import *

urlpatterns = [
    path('user/list/', ListFormUser.as_view(), name='usuario_ver'),
    path('user/create/', CreateFormUser.as_view(), name='usuario_crear'),
    path('user/update/<int:pk>', UpdateFormUser.as_view(), name='usuario_update'),
    path('user/delete/<int:pk>', DeleteFormUser.as_view(), name='usuario_delete'),
    path('user/update/password/<int:pk>', UpdatePasswordFormUser.as_view(), name='usuario_update_password'),
]