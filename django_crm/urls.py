

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/login/', auth_views.LoginView.as_view(template_name='users/login_form.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('create_clients/', include('clients.urls')),
    path('create_cleaners/', include('cleaners.urls')),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)