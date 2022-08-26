from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.create_clients, name='create_clients'),    
    path('create_status', views.create_status, name='create_status'),
    path('dashboard', views.clients_dashboard, name='dashboard'),
    path('show_client/<str:pk>', views.show_client, name='show_client'),
    path('get_email_template/<str:pk>', views.email_sending_system, name='get_email_template'),
    path('email_record/<str:pk>', views.previous_emails, name='email_record'),
    path('email_details/<str:pk>',views.email_details_of_a_specific_client, name='email_details'),

    path('create_pdf/<str:pk>', views.create_pdf, name='create_pdf'),

]


htmx_urlpatterns = [
    path("search_zip", views.show_cleaner_to_client, name="search_zip")
]

urlpatterns += htmx_urlpatterns
