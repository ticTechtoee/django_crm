from django.urls import path, include
from . import views

APP_NAME = 'users'

urlpatterns = [

    path('', views.welcome, name='welcome'),
  
    path('signup/',views.signupform, name='signup'),

    path('login_form/', views.login_form, name='login_form'),

]