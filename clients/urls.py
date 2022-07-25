from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.create_clients, name='create_clients'),    
    path('create_zip_code', views.create_zip_code, name='create_zip_code'),
    path('create_status', views.create_status, name='create_status'),
    path('dashboard', views.clients_dashboard, name='dashboard'),
    path('show_client/<str:pk>', views.show_client, name='show_client'),
    path('get_email_template/<str:pk>', views.get_email_template, name='get_email_template'),
    path('send_email', views.send_emails, name="send-email"),

]