from django.db import models

class BasicData(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    def __str__(self):
        return self.name
