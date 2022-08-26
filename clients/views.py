from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from cleaners.models import cleaners
from xhtml2pdf import pisa
from clients.models import clients, email_content, Email_add
from .forms import clientsForm, statusForm, sent_emailForm
from twilio.rest import Client
from dotenv import load_dotenv
import os

# To get the tokens from .env file

load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

#---------------------------------------------

@login_required(login_url='/login_form/')
def create_clients(request):
    title_of_page = 'Create Clients'
    form = clientsForm()
    if request.method == 'POST':
        form = clientsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            cleaner_id = request.POST['list_of_cleaners']
            c_info = cleaners.objects.get(id = cleaner_id)
            instance.zip_code = request.POST['zip_code']
            instance.cleaner_allocated = c_info
            instance.save()
            try:
                create_message(request.POST['name'], request.user.get_username(), request.POST['mobile_number'])
            except:
                print("cannot send the sms in clients")
            finally:
                return redirect('clients:dashboard')
        else:
                print(form.errors)
    context = {'form':form, 'title':title_of_page}
    return render(request, 'clients/create_clients.html', context)
    


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


def show_cleaner_to_client(request):
    get_data = cleaners.objects.filter(zip_code = request.POST.get('zip_code')).values('id','email')
    context = {'cleaners_list': get_data}
    return render(request, 'clients/cleaners_list.html', context)


@login_required(login_url='/login_form/')
def clients_dashboard(request):
    get_client = clients.objects.all()
    if 'srchByName' in request.POST:
        get_client = clients.objects.filter(name=request.POST.get('search'))
    elif 'srchByEmail' in request.POST:
        get_client = clients.objects.filter(email=request.POST.get('search'))
    elif 'srchByZip' in request.POST:
        get_client = clients.objects.filter(zip_code=request.POST.get('search'))
    elif 'srchByPD' in request.POST:
        get_client = clients.objects.filter(preferred_day=request.POST.get('search'))
    elif 'srchByType' in request.POST:
        get_client = clients.objects.filter(type=request.POST.get('search'))
    elif 'srchByDateAdded' in request.POST:
        get_client = clients.objects.filter(date_added=request.POST.get('search'))

    context = {'client_info': get_client}
    return render(request, 'clients/dashboard.html', context)


def email_sending_system(request,pk):
    form = sent_emailForm()
    get_the_data = clients.objects.get(id=pk)
    if request.method == 'POST':
        if 'send_email' in request.POST:
            form = sent_emailForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)

                sent_to = Email_add.objects.get(client_add = get_the_data.email)
                
                subject = form.cleaned_data.get('email_subject')
                email_body = form.cleaned_data.get('email_body')
                instance.email_add = sent_to
                instance.save()
                from_email = settings.EMAIL_HOST_USER
                to_email = (get_the_data.email,'')
                message = EmailMultiAlternatives(subject=subject, body=email_body, from_email=from_email, to=to_email)
                message.content_subtype = "html"
                message.send()
                return redirect('clients:email_record', pk=get_the_data.email)
            else:
                print(form.errors)
    context = {'form':form, 'clients_data':get_the_data}
    return render(request, 'clients/send_emails.html', context)

def previous_emails(request, pk):
    get_record = email_content.objects.filter(email_add__client_add = pk).values('id','email_subject')
    context = {'all_emails':get_record, 'email_add':pk}
    return render(request, 'clients/email_record.html', context)

def email_details_of_a_specific_client(request,pk):
    get_record = email_content.objects.filter(id = pk).values('email_subject','email_body')
    context = {'email_body':get_record}
    return render(request, 'email_details.html', context)


# SMS System

def create_message(clients_name, staff_name, to_number):
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body = 
                                'Hi, ' +clients_name+
                                ' your profile has been created by '+staff_name+ ' at maid2clean',
                                
                                from_='+447862127546',
                                to=to_number
                            )

    print(message.error_message)
    return "success"


#---------------------------------------------------------------------------------------

def show_client(request, pk):
    get_the_data = clients.objects.get(id=pk)
    context = {'client_detail':get_the_data}
    return render(request, 'clients/show_client.html', context)

def create_pdf(request,pk):
    c_info = clients.objects.get(id=pk)
    template_path = 'clients/create_report/export_pdf.html'
    context = {'client_detail': c_info}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="client_profile.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response