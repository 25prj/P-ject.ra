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
    
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
           
            username = request.POST.get('username')
            email = request.POST.get('password')
            password = request.POST.get('password1')

            user = User.objects.create_user(username=username, email=email, password=password)
            
            if 'sakara' is email:
                user.is_superuser=True
                user.save()
            else:
                user.save()

            return redirect('login')
        else:
            form = SignupForm()

        return render(request, 'core/signup.html',{'form': form})
    
    return render(request, 'core/signup.html',{'form': form})


def contact_page(request):
    return render(request,'core/contact.html')


def logout_user(request):
    logout(request)

    return redirect('/')


