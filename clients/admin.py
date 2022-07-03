from django.contrib import admin
from .models import clients, zipCode, status

# Register your models here.
admin.site.register(clients)
admin.site.register(zipCode)

admin.site.register(status)