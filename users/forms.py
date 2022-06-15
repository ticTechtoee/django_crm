from django.forms import ModelForm
from .models import BasicData
from django import forms

class BasicDataForm(ModelForm):
    class Meta:
        model = BasicData
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
            'email': forms.EmailInput(attrs={'placeholder': 'abc@gmail.com'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
        }
    def __init__(self, *args, **kwargs):
        super(BasicDataForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input',})