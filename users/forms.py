from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import clients, cleaners

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    contact_number = forms.CharField(max_length=10, required=False, help_text='Optional',widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Letters and Number'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'contact_number' ,'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
        }

class clientsForm(ModelForm):
    class Meta:
        model = clients
        fields = '__all__'

class cleanersForm(ModelForm):
    class Meta:
        model = cleaners
        fields = '__all__'