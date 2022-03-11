from django.shortcuts import render
from core.usersquid.models import Usersquid
from core.usersquid.forms import *
from core.category.forms import *
from django.http.response import HttpResponseRedirect, JsonResponse,HttpResponse
from django.urls import reverse_lazy


from django.views.generic import CreateView

class CreateFormPublicUser(CreateView):
    model = Usersquid
    form_class=UsersquidPublicForms
    template_name='register.html'
    success_url=reverse_lazy('usuario_ver')

    def post(self, request, *args, **kwargs):
        form = UsersquidPublicForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mensaje.html')
        self.object = None  
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return super().post(request, self.template_name, context)
    
    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['title1']="Creación de Usuarios SQUID"
            return context



