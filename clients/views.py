
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import clientsForm,zipCodeForm, statusForm

@login_required(login_url='/login_form/')
def create_clients(request):
    title_of_page = 'Create Clients'
    form = clientsForm()
    if request.method == 'POST':
        form = clientsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('The Clients Profile Has been done.')
        else:
            print(form.errors)
    context = {'form':form, 'title':title_of_page}
    return render(request, 'clients/create_clients.html', context)
    
@login_required(login_url='/login_form/')
def create_zip_code(request):
    
    form = zipCodeForm()
    if request.method == 'POST':
        form = zipCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:create_clients')
    context = {'form': form}
    return render(request, 'clients/create_zip_code.html', context)

@login_required(login_url='/login_form/')
def create_status(request): 
    form = statusForm()
    if request.method == 'POST':
        form = statusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:create_clients')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'clients/create_status.html', context)

