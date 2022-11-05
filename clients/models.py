import uuid
from django.db import models
from cleaners.models import cleaners
from ckeditor.fields import RichTextField
from datetime import datetime



NAME_OF_DAY=[
('MON', 'Monday'),
('TUE', 'Tuesday'),
('WED','Wednesday'),
('THU', 'Thursday'),
('FRI', 'Friday'),
('SAT', 'Saturday'),
('SUN', 'Sunday')
]
#regular or one-off
TYPE = [
    ('RE', 'Regular'),
    ('O-F', 'One Off')
]
#Weekly, monthly, fortnightly
FREQUENCY = [
    ('Weekly','Weekly'),
    ('Monthly','Monthly'),
    ('Fortnightly','Fortnightly')
]
#Question
ARE_THEY_PAYING = [
    ('Yes','Yes'),
    ('No', 'No')
]

#DD, Standing Order(SO), Card 
TYPES_PAYING_METHODS = [
    ('DD', 'DD'),
    ('SO', 'Standing Order(SO)'),
    ('CA', 'Card')
]



class clients(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    #Mr, Ms, Mrs
    #One Field is Fine
    name = models.CharField(max_length=50)
    
    #Three Line and A Zip code at the end
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30)
    address_line_3 = models.CharField(max_length=30)
    
    post_code = models.CharField(max_length=8, default="0")

    

    # 11 digits in the number
#    1 mobile and 1 landline.

    landline_number = models.CharField(max_length=11, null=True, blank=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)

    email = models.EmailField(unique=True, blank=False)

    #22-06-28 13:44
    date_added = models.DateField()

    #Notes in a text form
    
    # tba to be allocated, int interviewing cleaner, ncp cleaner accepted, dc dead client
    status = models.ForeignKey('status', on_delete = models.CASCADE)

    #Notes fields is missing, date stamp and description
    
    # Any day of week
    # Text field
    preferred_day = models.CharField(max_length=8, choices=NAME_OF_DAY)

    #regular or one-off
    type = models.CharField(max_length=6, choices=TYPE)

    #Weekly, monthly, fortnightly
    frequency = models.CharField(max_length=11, choices=FREQUENCY)

    #digits, 1-10
    number_of_hours = models.IntegerField()

    #Yes or No
    paying = models.CharField(max_length=3, choices=ARE_THEY_PAYING)
    
    #DD, Standing Order(SO), Card 
    paying_methods = models.CharField(max_length=13, choices=TYPES_PAYING_METHODS)
    
    # Every cleaner that is available in the postcode, existing cleaner status, available for work
    cleaner_allocated = models.ForeignKey(cleaners, on_delete=models.PROTECT, null = True, blank = True)
       
    
    #Surname of the client, reference to see the payments, text field
    payment_reference = models.CharField(max_length=40)
    
        
    #sms_to_client = models.CharField(max_length=1)

    notes =  models.TextField()

    def __str__(self):
        return self.email
        
 #Notes in a text form
# tba to be allocated, int interviewing cleaner, ncp cleaner accepted, dc dead client
class status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    abber_of_notes = models.CharField(max_length=4, default='tba')
    full_form = models.CharField(max_length=30, default='to be allocated')
    def __str__(self):
        return self.abber_of_notes


class ex_cleaner(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    client_id = models.UUIDField(default=uuid.uuid4)
    client_email = models.EmailField()
    cleaner =  models.ForeignKey(cleaners, on_delete = models.PROTECT, null = True, blank = True)

    def __str__(self):
        return self.cleaner.name

class EmailsSentToClient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email_recipient = models.ForeignKey('clients', on_delete = models.PROTECT) 
    email_subject = models.CharField(max_length = 50)
    email_content = RichTextField(blank = True, default="None")
