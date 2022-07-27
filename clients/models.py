from queue import Empty
import uuid
from django.db import models
from cleaners.models import cleaners
from ckeditor.fields import RichTextField

NAME_OF_DAY=[('MON', 'Monday'),
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
    ('1','Weekly'),
    ('2','Monthly'),
    ('3','Fortnightly')
]
#Question
ARE_THEY_PAYING = [
    ('1','Yes'),
    ('2', 'No')
]

#DD, Standing Order(SO), Card 
TYPES_PAYING_METHODS = [
    ('1', 'DD'),
    ('2', 'Standing Order(SO)'),
    ('3', 'Card')
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
    
    zip_code = models.ForeignKey('zipCode', on_delete=models.CASCADE)

    profile_image = models.ImageField(upload_to='images/profile_images/', null=True, blank=True)

    # 11 digits in the number
#    1 mobile and 1 landline.

    landline_number = models.CharField(max_length=11, null=True, blank=True)
    mobile_number = models.CharField(max_length=11, null=True, blank=True)

    email = models.EmailField()

    #22-06-28 13:44
    date_added = models.DateTimeField()

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
    frequency = models.CharField(max_length=10, choices=FREQUENCY)

    #digits, 1-10
    number_of_hours = models.IntegerField()

    #Yes or No
    paying = models.CharField(max_length=3, choices=ARE_THEY_PAYING)
    
    #DD, Standing Order(SO), Card 
    paying_methods = models.CharField(max_length=13, choices=TYPES_PAYING_METHODS)
    
    # Every cleaner that is available in the postcode, existing cleaner status, available for work
    cleaner_allocated = models.ForeignKey(cleaners, on_delete=models.PROTECT)
    
    # An ex-cleaner, 
    ex_cleaners = models.CharField(max_length=20)
    
    #Surname of the client, reference to see the payments, text field
    payment_reference = models.CharField(max_length=40)
    
    #Email address, make history of each converstation or letters
    
    email_to_client = models.ForeignKey('sent_emails', on_delete=models.PROTECT)
    
    
    #sms_to_client = models.CharField(max_length=1)

    def __str__(self):
        return self.name
        
 #Three Line and A Zip code at the end
class zipCode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    zip_code = models.CharField(max_length=5, blank=True, default='0')
    def __str__(self):
        return self.zip_code


#Notes in a text form
# tba to be allocated, int interviewing cleaner, ncp cleaner accepted, dc dead client
class status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    abber_of_notes = models.CharField(max_length=4, default='tba')
    full_form = models.CharField(max_length=30, default='to be allocated')
    def __str__(self):
        return self.abber_of_notes

FORMAT_EMAIL_TEMPLATES = [
    ('TEMP 1','Template 1'),
    ('TEMP 2','Template 2')
]

class email_templates(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    template_name = models.CharField(max_length=50, choices=FORMAT_EMAIL_TEMPLATES)
    def __str__(self):
        return self.template_name

class sent_emails(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email_subject = models.CharField(max_length=50)
    email_body = RichTextField(blank = True, null=True)
    def __str__(self):
        return self.email_subject