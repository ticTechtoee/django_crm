from django.urls import path, include
from . import views

app_name = 'cleaners'

urlpatterns = [
    path('', views.create_cleaners, name='create_cleaners'),    
    path('create_status', views.create_status, name='create_status'),
]