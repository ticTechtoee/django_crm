from django.contrib import admin
from .models import clients, status,Email_add,email_content


admin.site.register(clients)
admin.site.register(status)
admin.site.register(Email_add)
admin.site.register(email_content)