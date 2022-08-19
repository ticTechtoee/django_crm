from django.contrib import admin
from .models import clients, status, email_templates, sent_emails

# Register your models here.
admin.site.register(clients)

admin.site.register(status)
admin.site.register(email_templates)
admin.site.register(sent_emails)