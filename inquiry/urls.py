from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    path('', views.inquiryView, name='inquiry_view'),
    ]
