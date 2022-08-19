from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import clients, cleaners

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'John'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Doe'}))
    contact_number = forms.CharField(max_length=13, required=False, help_text='Optional',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '+445678901198'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'john@company.com'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password (e.g: _abc@123)'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'contact_number' ,'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'johndoe1'}),
        }

# class clientsForm(ModelForm):
#     class Meta:
#         model = clients
#         fields = '__all__'

# class cleanersForm(ModelForm):
#     class Meta:
#         model = cleaners
#         fields = '__all__'