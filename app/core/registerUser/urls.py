from django.urls import path
from core.registerUser.views.views import CreateFormPublicUser

urlpatterns = [
    path('', CreateFormPublicUser.as_view(), name='registrar'),

]