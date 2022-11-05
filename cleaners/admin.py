from django.contrib import admin
from .models import cleaners, status, EmailsSentToCleaners

admin.site.register(cleaners)
admin.site.register(status)
admin.site.register(EmailsSentToCleaners)