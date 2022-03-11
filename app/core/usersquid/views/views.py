from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from core.usersquid.views.views import *
from core.usersquid.models import Usersquid
from core.usersquid.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

class ListFormUser(ListView):
    model = Usersquid
    template_name = 'list_users.html'

    #mantener Datos
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de Usuarios SQUID'
        return context

class CreateFormUser(CreateView):
    model = Usersquid
    form_class=UsersquidForms
    template_name='create_users.html'
    success_url=reverse_lazy('usuario_ver')

    def post(self, request, *args, **kwargs):
        form = UsersquidForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return super().post(request, self.template_name, context)
    
    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['title1']="Creación de Usuarios SQUID"
            return context

class UpdateFormUser(UpdateView):
    model=Usersquid
    form_class = UpdateUsersquidForms
    template_name='create_users.html'
    success_url = reverse_lazy('usuario_ver')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Editar Usuario SQUID"
        return context

class UpdatePasswordFormUser(UpdateView):
    model=Usersquid
    form_class = UpdatePasswordUsersquidForms
    template_name='create_users.html'
    success_url = reverse_lazy('usuario_ver')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Editar Credenciales del Usuario"
        return context

class DeleteFormUser(DeleteView):
    model=Usersquid
    form_class = UsersquidForms
    template_name='delete_users.html'
    success_url = reverse_lazy('usuario_ver')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title1']="Eliminar usuario SQUID"
        return context