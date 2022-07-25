
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from clients.models import clients, email_templates

from .forms import clientsForm,zipCodeForm, statusForm, email_templateForm






@login_required(login_url='/login_form/')
def create_clients(request):
    title_of_page = 'Create Clients'
    form = clientsForm()
    if request.method == 'POST':
        form = clientsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clients:dashboard')
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

@login_required(login_url='/login_form/')
def clients_dashboard(request):
    get_client = clients.objects.all()
    if 'srchByName' in request.POST:
        get_client = clients.objects.filter(name=request.POST.get('search'))
    elif 'srchByEmail' in request.POST:
        get_client = clients.objects.filter(email=request.POST.get('search'))
    elif 'srchByZip' in request.POST:
        get_client = clients.objects.filter(zip_code__zip_code=request.POST.get('search'))
    elif 'srchByPD' in request.POST:
        get_client = clients.objects.filter(preferred_day=request.POST.get('search'))
    elif 'srchByType' in request.POST:
        get_client = clients.objects.filter(type=request.POST.get('search'))

    context = {'client_info': get_client}
    return render(request, 'clients/dashboard.html', context)


def send_emails(template_name, clients_email):
    subject = "Welcome to maid2clean"
    from_email = settings.EMAIL_HOST_USER
    to_email = (clients_email,'')
    with open("welcome_email.txt") as f:
        welcome_message = f.read()
    message = EmailMultiAlternatives(subject=subject, body=welcome_message, from_email=from_email, to=to_email)
    if template_name == 'TEMP 1':
        html_template = get_template("email_templates/price_template.html").render()
    else:
        html_template = get_template("email_templates/no_email_temp.html").render()
    message.attach_alternative(html_template,"text/html")
    message.send()
    return 'Email Sent'

def get_email_template(request,pk):
    form = email_templateForm()
    get_the_data = clients.objects.get(id=pk)
    if request.method == 'POST':
        select_value = request.POST.get('template_name')
        if select_value == 'TEMP 1':
            ans_frm_func =  send_emails(select_value, get_the_data.email)
            print(ans_frm_func)
        elif select_value == 'TEMP 2':
            send_emails(select_value,get_the_data.email)
    context = {'form': form, 'clients_data':get_the_data}
    return render(request, 'clients/send_emails.html', context)

def show_client(request, pk):
    get_the_data = clients.objects.get(id=pk)
    context = {'client_detail':get_the_data}
    return render(request, 'clients/show_client.html', context)



