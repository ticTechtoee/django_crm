
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, clientsForm, cleanersForm

def welcome(request):
    return render(request, 'users/welcome.html')


def create_staff(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:welcome')
    else:
        form = SignUpForm()
    return render(request, 'users/create_staff.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('users:create_staff')
            elif not user.is_superuser:    
                login(request, user)
                return redirect('users:create_clients_cleaners')
        else:
            return redirect('users:welcome')
    return render(request, 'users/login_form.html')


def create_clients(request):
    form = clientsForm()
    if request.method == 'POST':
        form = clientsForm()
        if form.is_valid():
            form.save()
            return HttpResponse('Cleaner Profile has been created')
    context = {'form':form}
    return render(request, 'users/create_clients.html', context)


def create_cleaners(request):
    form = cleanersForm()
    if request.method == 'POST':
        form = cleanersForm()
        if form.is_valid():
            form.save()
            return HttpResponse('Cleaner Profile has been created')
    context = {'form':form}
    return render(request, 'users/create_cleaners.html', context)