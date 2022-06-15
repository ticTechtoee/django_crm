from django.shortcuts import render, redirect

from django.contrib.auth import authenticate

from .models import BasicData
from .forms import BasicDataForm


def welcome(request):
    return render(request, 'users/welcome.html')

def login_form(request):
    if request.method == 'POST':
        return render(request, 'users/new_welcome_page.html')
    return render(request,'users/login_form.html')

def signupform(request):
    form = BasicDataForm()
    if request.method == 'POST':
        form = BasicDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_form')
    context = {'form':form}
    return render(request, 'users/signUp_form.html', context)

