from django.forms import ModelForm
from django import forms

from .models import cleaners, status, email_content
from datetime import datetime



class cleanersForm(ModelForm):

    class Meta:
        model = cleaners
        fields = '__all__'
        widgets = {
            'transactions_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'date_added': forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'referee_1_details':forms.Textarea(attrs={'rows':4, 'cols':4}),
            'referee_2_details':forms.Textarea(attrs={'rows':4, 'cols':4}),
            'notes':forms.Textarea(attrs={'rows':4, 'cols':4}),
            }



    def __init__(self, *args, **kwargs):
        super(cleanersForm, self).__init__(*args, **kwargs)
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

class updateStatusForm(ModelForm):
    class Meta:
        model = cleaners
        fields = ('status',)
        
    def __init__(self, *args, **kwargs):
        super(updateStatusForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})