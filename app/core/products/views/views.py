from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from core.products.views.views import *
from core.products.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView



class ListFormProduct(ListView):
    model = Producto
    template_name = 'list_producto.html'

    #mantener Datos
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de Productos'
        return context

class CreateFormProduct(CreateView):
    model = Producto
    form_class=ProductoForms
    template_name='create_products.html'
    success_url=reverse_lazy('producto_ver')

    def post(self, request, *args, **kwargs):
        form = ProductoForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return super().post(request, self.template_name, context)
    
    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['title1']="Creacion de Usuarios"
            return context

class UpdateFormProduct(UpdateView):
    model=Producto
    form_class = ProductoForms
    template_name='create_products.html'
    success_url = reverse_lazy('producto_ver')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']="Editar usuario"
        return context

class DeleteFormProduct(DeleteView):
    model=Producto
    form_class = ProductoForms
    template_name='delete_products.html'
    success_url = reverse_lazy('producto_ver')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Eliminar usuario"
        return context