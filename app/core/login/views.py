from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


class LoginFormView(LoginView):
    template_name='login.html'

    def dispatch(self, request, *args, **kwargs) :

        if request.user.is_authenticated:
            return redirect('/categoria/category/home/')    
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title']='Inicio Session'
        context['subtitle']='Squid'
        return context


