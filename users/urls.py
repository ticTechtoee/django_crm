from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [

    path('', views.welcome, name='welcome'),
  
    path('create_staff/',views.create_staff, name='create_staff'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('login_form/', views.loginUser, name='login_form'),
    path('logout/', views.logout_user, name='logut_user'),
    

    # path('create_clients/', views.create_clients, name='create_clients'),
    # path('create_cleaners/', views.create_cleaners, name='create_cleaners'),
    

]