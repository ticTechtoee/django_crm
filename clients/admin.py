from django.contrib import admin
from .models import clients, zipCode, status, email_templates

# Register your models here.
admin.site.register(clients)
admin.site.register(zipCode)

admin.site.register(status)
admin.site.register(email_templates)