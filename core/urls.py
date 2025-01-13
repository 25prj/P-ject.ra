from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_page/', views.contact_page, name='contact'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),

    #password resetting
    #path('change-password/',auth_views.PasswordChangeView.as_view(), name='password_change'),
    
]
