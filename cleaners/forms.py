from django.forms import ModelForm
from django import forms

from .models import cleaners, status



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