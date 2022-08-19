from django.urls import path, include
from . import views

app_name = 'cleaners'

urlpatterns = [
    path('', views.create_cleaners, name='create_cleaners'),    
    path('create_status', views.create_status, name='create_status'),
    path('dashboard', views.cleaners_dashboard, name='dashboard'),
    path('send_email/<str:pk>', views.get_email_template, name="send-email"),
    path('update_status/<str:pk>', views.updateStatus, name='update_status'),
]