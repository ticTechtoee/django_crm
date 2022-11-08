from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twilio.rest import Client
from .forms import SignUpForm
from dotenv import load_dotenv
import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings

from django.contrib import messages


load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


def create_message(staff_name, admin_name, to_number):
   
    account_sid = account_sid
    auth_token = auth_token

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



def welcome(request):
    return render(request, 'users/welcome.html')

@login_required(login_url='/login_form/')
def create_staff(request):
    title_of_page = 'Create Staff'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                create_message(request.POST['first_name'], request.user.get_username(), request.POST['contact_number'])
            except:
                print("cannot send the message in users")
            finally:
                return redirect('users:dashboard')
            
    else:
        form = SignUpForm()
    return render(request, 'users/create_staff.html', {'form': form, 'title':title_of_page})


@login_required(login_url='/login_form/')
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
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'users/login_form.html')

def logout_user(request):
    logout(request)
    return redirect('users:login_form')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'maid2clean',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})