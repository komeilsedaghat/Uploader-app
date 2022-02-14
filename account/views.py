from urllib import request
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,FormView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginUserForm,RegisterUserForm,TFAForm,ActivateTFAForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from django.contrib.auth import login,authenticate
from account.models import User
import random
from django.core.mail import send_mail
from django.conf import settings



class LoginUserView(SuccessMessageMixin,FormView):
    template_name = "account/auth/login.html"
    form_class = LoginUserForm
    success_url =reverse_lazy('account:TFA')
    

    def form_valid(self,form):
        global number
        global username
        global password
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        number = random.randrange(100000,999999)
        subject = 'authentication code'
        message = f"Hi {username} \U0001F607 \n Your Verification Code {number} \n Have a Good Day"
        email_from = settings.EMAIL_HOST_USER
        user = get_object_or_404(User,username = username)
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        print(user.TwoFactorAuthentication)    
        
        return redirect('account:TFA')
    
    def get_success_message(self, cleaned_data):
        return f"Welcome {self.request.user}"



class TwoFactorAuthenticationView(FormView):
    template_name = 'account/auth/TFA.html'
    form_class = TFAForm
    suceess_url = reverse_lazy('/')

    def form_valid(self,form):
        token_input = form.cleaned_data['token_number']
        if token_input == number:
            user = authenticate(self.request, username=username, password=password)
            login(self.request,user)
            messages.success(self.request,f'Welcome {username}')
            return redirect('/')
        else:
            messages.error(self.request,"Your Two Factor Authenticaion Code Is Wrong Please Try Again")
            return redirect('account:login')
    


class LogoutUserView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')



class RegisterUserView(CreateView):
    template_name = "account/auth/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('account:login')



class ActiveTFAView(LoginRequiredMixin,FormView):
    template_name = 'account/auth/activeTFA.html'
    form_class = ActivateTFAForm
    success_url = reverse_lazy('file:home')
