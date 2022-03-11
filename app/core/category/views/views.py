from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.category.views.views import *
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView

from core.category.models import Categoria
from core.category.forms import CategoryForm
from core.category.mixmin import IsSuperUser


class home(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs) 
        context['title']='hola'
        return context

class CategoriaListView(LoginRequiredMixin, IsSuperUser, ListView):

    model = Categoria
    template_name = 'list_category.html'


    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('producto_ver')
    #mantener Datos
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title1']='Listado de Categorias'
        return context


class CategoriaCreateView(CreateView):
    model=Categoria
    form_class = CategoryForm
    template_name='create_category.html'
    success_url = reverse_lazy('categoria_list')

    def post(self, request, *args, **kwargs) :
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

        

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Creación de categoria"
        context['form']=CategoryForm()
        return context


class CategoriaUpdateView(UpdateView):
    model=Categoria
    form_class = CategoryForm
    template_name='create_category.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']="Editar de categoria"
        return context


class CategoriaDeleteView(DeleteView):
    model=Categoria
    form_class = CategoryForm
    template_name='delete_category.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']="Eliminar categoria"
        return context


class CategoriaFormView(FormView):
    form_class=CategoryForm
    template_name='category/create.html'
    success_url=reverse_lazy('category/list.html')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']="Formulario de categoria"
        return context

