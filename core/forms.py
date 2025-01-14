from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'username',
        'class':'py-2 h-10 px-2  w-full focus:outline-none',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'password',
        'class':'py-2 px-2 w-full focus:outline-none',
    }))


class SignupForm(UserCreationForm):


    class Meta:
        model = User 
        fields = ["username", "email","password1", "password2"]


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="Username" ,required=True)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'example@gmail.com',
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="Email", required=True)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password'.title(),
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="Password", required=True)
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'.title(),
        'class':'py-2 px-2 w-full focus:outline-none'
    }), label="Confirm Password", required=True)