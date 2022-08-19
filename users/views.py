
from multiprocessing import context
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twilio.rest import Client
from .forms import SignUpForm

def welcome(request):
    return render(request, 'users/welcome.html')

@login_required(login_url='/login_form/')
def create_staff(request):
    title_of_page = 'Create Staff'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            create_message(request.POST['first_name'] + request.POST['last_name'], request.user.get_username(), request.POST['contact_number'])
            return redirect('users:dashboard')
            
    else:
        form = SignUpForm()
    return render(request, 'users/create_staff.html', {'form': form, 'title':title_of_page})



def dashboard(request):
    get_users = User.objects.all()
    context = {'users_info': get_users}
    return render(request, 'users/dashboard.html', context)




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
                return redirect('clients:create_clients')
        else:
            return redirect('users:welcome')
    return render(request, 'users/login_form.html')

def logout_user(request):
    logout(request)
    return redirect('users:login_form')

def create_message(staff_name, admin_name, to_number):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC3822a9e7572f87dcfcf773200c2371c3'
    auth_token = 'e03f8b1617fa252c2d874839c6511c7f'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body = 
                                'Hi, ' +staff_name+
                                ' your profile has been created by '+admin_name+ ' at maid2clean',
                                
                                from_='+447862127546',
                                to=to_number
                            )

    print(message.error_message)
    return "success"