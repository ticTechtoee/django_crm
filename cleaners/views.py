from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from cleaners.models import cleaners


from .forms import cleanersForm,statusForm

@login_required(login_url='/login_form/')
def create_cleaners(request):
    title_of_page = 'Create Cleaners'
    form = cleanersForm()
    if request.method == 'POST':
        if request.POST.get('btnsave'):
            form = cleanersForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('cleaners:dashboard')
            else:
                print(form.errors)
    context = {'form':form, 'title':title_of_page}
    return render(request, 'cleaners/create_cleaners.html', context)

@login_required(login_url='/login_form/')
def create_status(request): 
    form = statusForm()
    if request.method == 'POST':
        form = statusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cleaners:create_cleaners')
    context = {'form': form}
    return render(request, 'cleaners/create_status.html', context)

@login_required(login_url='/login_form/')
def cleaners_dashboard(request):
    get_cleaner = cleaners.objects.all()
    context = {'cleaner_info': get_cleaner}
    return render(request, 'cleaners/dashboard.html', context)
