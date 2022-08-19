from django.forms import ModelForm
from django import forms

from .models import cleaners, status, sent_emails



class cleanersForm(ModelForm):

    class Meta:
        model = cleaners
        fields = '__all__'
        widgets = {
            'transactions_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'date_added': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),}

    def __init__(self, *args, **kwargs):
        super(cleanersForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
    
    
class statusForm(ModelForm):
    class Meta:
        model = status
        fields = '__all__'

class sent_emailForm(ModelForm):
    
    class Meta:
        model = sent_emails
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(sent_emailForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class updateStatusForm(ModelForm):
    class Meta:
        model = cleaners
        fields = ('status',)
        
    def __init__(self, *args, **kwargs):
        super(updateStatusForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})