
from django.forms import ModelForm
from django import forms

from .models import clients, status, email_content
from datetime import datetime



class clientsForm(ModelForm):

    class Meta:
        model = clients
        
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
                'address_line_1': forms.TextInput(attrs={'placeholder': 'Address Line 1'}),
                'address_line_2': forms.TextInput(attrs={'placeholder': 'Address Line 2'}),
                'address_line_3': forms.TextInput(attrs={'placeholder': 'Address Line 3'}),
               
                'landline_number': forms.TextInput(attrs={'placeholder': 'Telephone Number'}),
                'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
                'email': forms.EmailInput(attrs={'placeholder': 'abc@gmail.com'}),
                'date_added': forms.DateInput(attrs={'type': 'date'}),
                'number_of_hours': forms.NumberInput(attrs={'placeholder':'Number of Hours'}),
                'payment_reference': forms.TextInput(attrs={'placeholder':'Surname'}),
                'notes':forms.Textarea(attrs={'rows':10}),
               

        }
        exclude = ['cleaner_allocated']
    
    
    def __init__(self, *args, **kwargs):
        super(clientsForm, self).__init__(*args, **kwargs)
        
        self.fields['notes'].initial = str(datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class statusForm(ModelForm):
    class Meta:
        model = status
        fields = '__all__'


class sent_emailForm(ModelForm):
    
    class Meta:
        model = email_content
        fields = '__all__'
        exclude = ['email_add']
    def __init__(self, *args, **kwargs):
        super(sent_emailForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
