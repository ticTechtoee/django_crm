from email.policy import default
from operator import mod
from random import choices
from django.db import models

class Inquiry(models.Model):
    ROLE =[ ('Client','Client'),
    ('Cleaner','Cleaner')
    ]
    STATUS = [('Pending','Pending'),
    ('Allocated','Allocated')
    ]
    name = models.CharField(default = "None", max_length = 50)
    email = models.EmailField()
    contact_number = models.CharField(max_length = 13)
    role = models.CharField(max_length=7, choices=ROLE)
    status = models.CharField(max_length = 9, choices=STATUS, default = "Pending")

    def __str__(self):
        return self.name
