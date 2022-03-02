from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


# Create your views here.
class LoginFormView(LoginView):
    template_name='ingreso.html'

    def dispatch(self, request, *args, **kwargs) :

        if request.user.is_authenticated:
            return redirect('https://www.google.com.mx/')    
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']='Inicio Session'
        context['subtitle']='USUARIO'
        return context
