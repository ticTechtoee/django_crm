
from django.db import models
from django.contrib.auth.models import User

class staff_profile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13, default='None')
