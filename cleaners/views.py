from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


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
                
            else:
                print(form.errors)
    context = {'form':form}
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


def logout(request):
    if 'btnlogout' in request.POST:
        logout(request)
        return redirect('users:login_form')
    return redirect('cleaners:create_cleaners')



