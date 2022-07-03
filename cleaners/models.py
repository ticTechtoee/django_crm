from django.db import models
import uuid


# Create your models here.

#Question
QUESTION = [
    ('1','Yes'),
    ('2', 'No')
]


class cleaners(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=30)
    address_line2 = models.CharField(max_length=30)
    address_line3 = models.CharField(max_length=30)
    post_code = models.CharField(max_length=6)

    landline_number = models.CharField(max_length=11)
    mobile_number = models.CharField(max_length=11)

    email = models.EmailField()
    
    date_added = models.DateField()
    #applicant(not interviwed), TBA, Full(No more work), DNU(do not use),lOA (left of owner code) 
    status = models.ForeignKey('status', on_delete = models.CASCADE)
    #digit 1-30 (any number)
    number_of_hours_wanted = models.IntegerField()
    # Free text
    nationality = models.CharField(max_length=20)
    #N if nationality is other than UK then it's needed (in form of image or file something)
    
    permit_to_work_needed = models.CharField(max_length=3, choices=QUESTION)
    
    #digit 11
    emergency_contact_number = models.CharField(max_length=11)
    emergency_contact_name = models.CharField(max_length=11)

    #Husband, mother, father any blood relation
    relationship_to_emergency_contact = models.CharField(max_length=10)

    #Disclouser system which will check for the character certificate
    Disclouser = models.CharField(max_length=3,choices=QUESTION)

    #National Insurance Number (9 digit number)
    NI_Nunber = models.CharField(max_length=9)

    #applying on behalf of cleaner for DBS
    consent_for_DBS = models.CharField(max_length=3,choices=QUESTION)
    #picture

    #Yes No question
    smoker = models.CharField(max_length=3,choices=QUESTION)
    
    #Yes No question
    can_iron = models.CharField(max_length=3,choices=QUESTION)
    #Yes No question
    driver = models.CharField(max_length=3,choices=QUESTION)
    #Yes No question
    has_car = models.CharField(max_length=3, choices=QUESTION)
    #id_proof
    #Name address, telnumber, relationship, company name 
    referee_1_details = models.CharField(max_length=50)
    #Name address, telnumber, relationship, company name
    referee_2_details = models.CharField(max_length=50)

    #Post Code with Area Names
    areas_worked = models.CharField(max_length=50)

    #Free Text
    prev_work_experience = models.CharField(max_length=30)

    #yes no
    prev_convicted_of_offence = models.CharField(max_length=3,choices=QUESTION)
    #Yes, No question

    # if yes then another field with the type of allergy
    pet_allergies = models.CharField(max_length=3,choices=QUESTION)

    type_of_allergy = models.CharField(max_length=12, default="None")

    #Record of payment from the client
    #if yes then put the, amount, date of transaction

    transactions_date = models.DateField()

    #Same as clients
    #email_client = models.CharField(max_length=20)
    #SMS_cleaner = models.CharField(max_length=20)

#Notes in a text form
# tba to be allocated, int interviewing cleaner, ncp cleaner accepted, dc dead client
class status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    abber_of_notes = models.CharField(max_length=4, default='tba')
    full_form = models.CharField(max_length=30, default='to be allocated')
    def __str__(self):
        return self.abber_of_notes