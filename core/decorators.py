from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def admin_only(admin_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return admin_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page')
    
    return wrapper