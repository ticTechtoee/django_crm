from django.urls import path, include
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.create_clients, name='create_clients'),    
    path('create_zip_code', views.create_zip_code, name='create_zip_code'),
     path('create_status', views.create_status, name='create_status'),
]