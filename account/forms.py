from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields= ('username','password',)

    def __init__(self,*args,**kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class':'input100'}
        self.fields['password'].widget.attrs = {'class':'input100'}



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ('username','email','password1','password2',)

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class':'input100'}
        self.fields['email'].widget.attrs = {'class':'input100'}
        self.fields['password1'].widget.attrs = {'class':'input100'}
        self.fields['password2'].widget.attrs = {'class':'input100'}

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('password not match')
        else:
            if len(password2) < 8:
                raise forms.ValidationError('your password most be more then 8 number')
            else:
                pass
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists')
        else:
            pass

