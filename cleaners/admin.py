from django.contrib import admin
from .models import cleaners, status

admin.site.register(cleaners)
admin.site.register(status)