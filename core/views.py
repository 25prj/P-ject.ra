from django.shortcuts import render, redirect
from django.contrib.auth import logout,login,authenticate
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            #check whether user is an admin
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('/')
        else:
            
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})
    return render(request, 'core/login.html', {'form': LoginForm()})


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = User.objects.create_user(username=username, email=email, password=password)
        
        #check and make email admin
        if 'sakara' in email:
            user.is_superuser = True
            user.save()

        return redirect('/')
        
        
    return render(request, 'core/signup.html',{'form': SignupForm()})


def logout_user(request):
    logout(request)

    return redirect('/')


