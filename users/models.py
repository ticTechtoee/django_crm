# import uuid
# from django.db import models

# class clients(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     #Mr, Ms, Mrs
#     #One Field is Fine
#     name = models.CharField(max_length=50)
#     #Three Line and A Zip code at the end
#     address = models.ForeignKey(address, on_delete=models.CASCADE)

   
#     # 11 digits in the number
#     # 1 mobile and 1 landline.
#     tel_number = models.CharField(max_length=10)
    
#     email = models.EmailField()
#     #22-06-28 13:44
#     date_added = models.DateField()
#     #Notes in a text form
#     # tba to be allocated, int interviewing cleaner, ncp cleaner accepted, dc dead client
    
#     status = models.ForeignKey('status', on_delete = models.CASCADE)
    
#     # Any day of week
#     # Text field
#     preferred_day = models.DateField()
#     #regular or one-off
#     type = models.CharField(max_length=5)
#     #Weekly, monthly, fortnightly
#     frequency = models.CharField(max_length=10)
#     #digits, 1-10
#     number_of_hours = models.IntegerField()
#     #Yes or No
#     paying = models.CharField(max_length=1)
#     #DD, Standing Order(SO), Card 
#     paying_methos = models.CharField(max_length=5)
#     # Every cleaner that is available in the postcode, existing cleaner status, available for work
#     cleaner_allocated = models.CharField(max_length=20)
#     # An ex-cleaner, 
#     ex_cleaners = models.CharField(max_length=20)
#     #Surname of the client, reference to see the payments, text field
#     payment_reference = models.CharField(max_length=40)
#     #Email address, make history of each converstation or letters
#     email_to_client = models.CharField(max_length=1)
#     #
#     sms_to_client = models.CharField(max_length=1)

# class status(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     notes = models.CharField(max_length=50)

#  #Three Line and A Zip code at the end
# class address(models.Model):
#     address_line_1 = models.CharField(max_length=30)
#     address_line_2 = models.CharField(max_length=30)
#     address_line_3 = models.CharField(max_length=30)
#     zip_code = models.CharField(max_length=5)

# """class contact_number(models.Model)"""


# class cleaners(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     post_code = models.CharField(max_length=6)
#     tel_number = models.CharField(max_length=10)
#     email = models.EmailField()
#     date_added = models.DateField()
#     #applicant(not interviwed), TBA, Full(No more work), DNU(do not use),lOA (left of owner code) 
#     status = models.ForeignKey(status, on_delete = models.CASCADE)
#     #digit 1-30 (any number)
#     number_of_hours_wanted = models.IntegerField()
#     # Free text
#     nationality = models.CharField(max_length=20)
#     #N if nationality is other than UK then it's needed (in form of image or file something)
#     permit_to_work_needed = models.CharField(max_length=1)
#     #digit 11
#     emergency_contact_number = models.CharField(max_length=10)
#     emergency_contact_name = models.CharField(max_length=10)
#     #Husband, mother, father any blood relation
#     relationship_to_emergency_contact = models.CharField(max_length=10)
#     #Disclouser system which will check for the character certificate
#     DBS = models.CharField(max_length=20)
#     #National Insurance Number (9 digit number)
#     NI_Nunber = models.CharField(max_length=30)
#     #applying on behalf of cleaner for DBS
#     consent_for_DBS = models.CharField(max_length=10)
#     #picture
#     #Yes No question
#     smoker = models.CharField(max_length=1)
#     #Yes No question
#     can_iron = models.CharField(max_length=1)
#     #Yes No question
#     driver = models.CharField(max_length=1)
#     #Yes No question
#     has_car = models.CharField(max_length=1)
#     #id_proof
#     #Name address, telnumber, relationship, company name 
#     referee_1_details = models.CharField(max_length=50)
#     #Name address, telnumber, relationship, company name
#     referee_2_details = models.CharField(max_length=50)
#     #Post Code with Area Names
#     areas_worked = models.CharField(max_length=50)
#     #Free Text
#     prev_work_experience = models.CharField(max_length=1)
#     #yes no
#     prev_convicted_of_offence = models.CharField(max_length=1)
#     #Yes, No question
#     # if yes then another field with the type of allergy
#     pet_allergies = models.CharField(max_length=1)
#     #Record of payment from the client
#     #if yes then put the, amount, date of transaction
#     transactions_date = models.DateField()
#     #Same as clients
#     email_client = models.CharField(max_length=20)
#     SMS_cleaner = models.CharField(max_length=20)
