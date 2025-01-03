from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'username',
        'class':'py-4 px-4 mb-3 w-full rounded-xl border-black',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'password',
        'class':'py-4 px-4 w-full rounded-xl border-black',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["username", "email","password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'w-full py-4 px-4 mb-4 rounded-xl'
    }), label="Username")

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'example@gmail.com',
        'class':'w-full py-4 px-4 mb-4 rounded-xl'
    }), label="Email")

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password'.title(),
        'class':'w-full py-4 px-4 mb-4 rounded-xl'
    }), label="Password")
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'.title(),
        'class':'w-full py-4 px-4 mb-4 rounded-xl'
    }), label="Confirm Password")