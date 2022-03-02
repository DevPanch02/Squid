from django.urls import path
from core.paginas.views.views import *

urlpatterns = [
    path('page/list/', ListFormPaginas.as_view(), name='list_page'),
    path('page/create/', CreateFormPage.as_view(), name='create_page'),
    path('page/update/<int:pk>', UpdateFormPage.as_view(), name='update_page'),
    path('page/delete/<int:pk>', DeleteFormPage.as_view(), name='delete_page'),
]