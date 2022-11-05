from django.contrib import admin
from .models import clients, status,ex_cleaner,EmailsSentToClient


admin.site.register(clients)
admin.site.register(status)
admin.site.register(EmailsSentToClient)
admin.site.register(ex_cleaner)