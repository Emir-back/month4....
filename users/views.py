from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView
from . import forms , models

class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'users/register.html'
    success_url = '/login/'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse ('users:user_list')
    
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
    