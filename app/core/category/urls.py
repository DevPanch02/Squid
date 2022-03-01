from django.urls import path
from core.category.views.views import *

urlpatterns = [
    
    path('category/home/', home.as_view(), name='home'),
    path('category/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('category/create/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('category/edit/<int:pk>', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('category/delete/<int:pk>', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('category/form/', CategoriaFormView.as_view(), name='categoria_form'),


    
]