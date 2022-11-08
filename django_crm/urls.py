from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    #path('admin/login/', auth_views.LoginView.as_view(template_name='users/login_form.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('create_clients/', include('clients.urls')),
    path('create_cleaners/', include('cleaners.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
   
    path('', include('django.contrib.auth.urls')),
    path('password_reset', views.password_reset_request, name='password_reset'),
       
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      
  ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)