from django.contrib import admin
from .models import cleaners, status, email_content, Email_add

admin.site.register(cleaners)
admin.site.register(status)
admin.site.register(email_content)
admin.site.register(Email_add)