
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.shortcuts import render, redirect

from cleaners.models import cleaners, status

from twilio.rest import Client

from .forms import cleanersForm,statusForm,sent_emailForm, updateStatusForm

@login_required(login_url='/login_form/')
def create_cleaners(request):
    title_of_page = 'Create Cleaners'
    form = cleanersForm()
    if request.method == 'POST':
        if 'btnsave' in request.POST:
            form = cleanersForm(request.POST, request.FILES)
            
            if form.is_valid():
                form.save()
                create_message(request.POST['name'], request.user.get_username(), request.POST['mobile_number'])
                return redirect('cleaners:dashboard')
            else:
                print(form.errors)
        else:
            print('No button')
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

    if 'srchByName' in request.POST:
        get_cleaner = cleaners.objects.filter(name=request.POST.get('search'))
    elif 'srchByEmail' in request.POST:
        get_cleaner = cleaners.objects.filter(email=request.POST.get('search'))
    elif 'srchByZip' in request.POST:
        get_cleaner = cleaners.objects.filter(zip_code=request.POST.get('search'))
    elif 'srchByPD' in request.POST:
        get_cleaner = cleaners.objects.filter(preferred_day=request.POST.get('search'))
    elif 'srchByType' in request.POST:
        get_cleaner = cleaners.objects.filter(type=request.POST.get('search'))
    elif 'srchByDateAdded' in request.POST:
        get_cleaner = cleaners.objects.filter(date_added=request.POST.get('search'))

    context = {'cleaner_info': get_cleaner}
    return render(request, 'cleaners/dashboard.html', context)


def get_email_template(request,pk):
    
    formSE = sent_emailForm()

    get_the_data = cleaners.objects.get(id=pk)
    if request.method == 'POST':
        if 'send_email' in request.POST:
            formSE = sent_emailForm(request.POST)
            if formSE.is_valid():
                formSE.save()
                
                #Custom Email 
                subject = formSE.cleaned_data.get('email_subject')
                email_body = formSE.cleaned_data.get('email_body')
                from_email = settings.EMAIL_HOST_USER
                to_email = (get_the_data.email,'')
                message = EmailMultiAlternatives(subject=subject, body=email_body, from_email=from_email, to=to_email)
                message.content_subtype = "html"
                message.send()
                return HttpResponse('Email Sent')

            else:
                print(formSE.errors)
    
    context = {'formSE':formSE, 'cleaners_data':get_the_data}
    return render(request, 'cleaners/send_emails.html', context)

def updateStatus(request, pk):
    form = updateStatusForm()
    if request.method == 'POST':
        new_status = request.POST['status']
        cleaners.objects.filter(pk=pk).update(status=new_status)
        return redirect('cleaners:dashboard')
    context = {'form': form}
    return render(request, 'cleaners/update_status.html', context)


def create_message(cleaners_name, staff_name, to_number):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC3822a9e7572f87dcfcf773200c2371c3'
    auth_token = 'e03f8b1617fa252c2d874839c6511c7f'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body = 
                                'Hi, ' +cleaners_name+
                                ' your profile has been created by '+staff_name+ ' at maid2clean',
                                
                                from_='+447862127546',
                                to=to_number
                            )

    print(message.error_message)
    return "success"