from urllib import request
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import View,CreateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginUserForm,RegisterUserForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

        

class LoginUserView(SuccessMessageMixin,LoginView):
    template_name = "account/auth/login.html"
    form_class = LoginUserForm
    success_url =reverse_lazy('file:home')
    
    def get_success_message(self, cleaned_data):
        return f"Welcome {self.request.user}"

class LogoutUserView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



class RegisterUserView(CreateView):
    template_name = "account/auth/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('account:login')