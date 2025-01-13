from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

from core.decorators import admin_only

@admin_only
def admin_dashboard(request):
    if request.user.is_authenticated:
    
        return render(request, 'admin_dashboard/admin_dashboard.html')
    else:
        return redirect('login')