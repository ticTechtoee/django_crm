import email
from email.policy import default
from pyexpat import model
from django.db import models

class Inquiry(models.Model):
    ROLE =[ ('Client','Client'),
    ('Cleaner','Cleaner')
    ]
    name = models.CharField(default = "None", max_length = 50)
    email = models.EmailField()
    contact_number = models.CharField(max_length = 13)
    role = models.CharField(max_length=7, choices=ROLE)
    def __str__(self):
        return self.name
