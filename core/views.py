from django.shortcuts import render, redirect
from django.contrib.auth import logout,login,authenticate
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.
from .decorators import unauthenticated_user

def index(request):
    return render(request, 'core/index.html')


@unauthenticated_user # return login url to homepage if user is already logged in
def login_user(request):
   
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            #check whether user is an admin or regular user
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('/')
        else:
            messages.info(request, f'incorrect username or password')
            return render(request, 'core/login.html',{'form':LoginForm()})
    return render(request, 'core/login.html', {'form':LoginForm()})


@unauthenticated_user # return login url to homepage if user is already logged in
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(username) < 3: #check if username is less than 3 characters
            messages.error(request, 'username should be 3 characters or more.')
        elif User.objects.filter(email=email).exists(): #check if email already exists
            messages.error(request, f'This email has an account already exists.')
            
        elif len(password1) < 8:
            messages.error(request, 'password is less than 8 characters.')
        elif password1 != password2:
            messages.error(request, 'passwords do not match')
        else:
            password = request.POST.get('password2')
            user = User.objects.create_user(username=username, email=email, password=password)
            
            if 'sakara' in email:
                user.is_superuser = True
                user.save()
            else:
                user.save()

            return redirect('login')
    
    return render(request, 'core/signup.html',{'form': SignupForm()})


def contact_page(request):
    return render(request,'core/contact.html')


def logout_user(request):
    logout(request)

    return redirect('/')


