from django.urls import path, include
from . import views

app_name = 'cleaners'

urlpatterns = [
    path('', views.create_cleaners, name='create_cleaners'),    
    path('create_status', views.create_status, name='create_status'),
    path('dashboard', views.cleaners_dashboard, name='dashboard'),
    path('send_emails/<str:pk>', views.email_sending_system, name='send-emails'),
    path('email_record/<str:pk>', views.previous_emails, name='email_record'),
    path('email_details/<str:pk>',views.email_details_of_a_specific_client, name='email_details'),
    path('update_status/<str:pk>', views.updateStatus, name='update_status'),
    path('profile_template', views.profile_template, name='profile_template'),
    
]

htmx_urlpatterns = [
    path("permit_image", views.permit_image, name="permit_image"),
    path("pet_allergies", views.pet_allergies, name="pet_allergies"),
]
urlpatterns += htmx_urlpatterns