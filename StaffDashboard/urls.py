
from django.urls import path, include
from . import views

app_name = 'StaffDashboard'

urlpatterns = [
    path('', views.dashboard, name='staff_dashboard'),
    path('update_inquiry/<str:pk>', views.UpdateInquiry, name='update_inquiry')
   ]
