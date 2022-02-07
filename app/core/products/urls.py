from django.urls import path
from core.products.views.views import *

urlpatterns = [
    path('user/list/', ListFormProduct.as_view(), name='producto_ver'),
    path('user/create/', CreateFormProduct.as_view(), name='producto_crear'),
    path('user/update/<int:pk>', UpdateFormProduct.as_view(), name='producto_update'),
    path('user/delete/<int:pk>', DeleteFormProduct.as_view(), name='producto_delete'),
    

]