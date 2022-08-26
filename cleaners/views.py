from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import render, redirect
from cleaners.models import cleaners, email_content, Email_add
from twilio.rest import Client
from .forms import cleanersForm, statusForm, sent_emailForm, updateStatusForm
from dotenv import load_dotenv
import os

# to get the token from .env files
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

# -------------------------------------------------------------------------------------------------------
@login_required(login_url="/login_form/")
def create_cleaners(request):
    title_of_page = "Create Cleaners"
    form = cleanersForm()
    if request.method == "POST":
        if "btnsave" in request.POST:
            form = cleanersForm(request.POST, request.FILES)
            if form.is_valid():
                email_add = Email_add.objects.create(
                    client_add=form.cleaned_data.get("email")
                )
                email_add.save()
                form.save()
                try:
                    create_message(
                        request.POST["name"],
                        request.user.get_username(),
                        request.POST["mobile_number"],
                    )
                except:
                    print("Cannot send the sms in cleaners")
                finally:
                    return redirect("cleaners:dashboard")
            else:
                print(form.errors)
        else:
            print("No button")
    context = {"form": form, "title": title_of_page}
    return render(request, "cleaners/create_cleaners.html", context)


@login_required(login_url="/login_form/")
def cleaners_dashboard(request):
    get_cleaner = cleaners.objects.all()

    if "srchByName" in request.POST:
        get_cleaner = cleaners.objects.filter(name=request.POST.get("search"))
    elif "srchByEmail" in request.POST:
        get_cleaner = cleaners.objects.filter(email=request.POST.get("search"))
    elif "srchByZip" in request.POST:
        get_cleaner = cleaners.objects.filter(zip_code=request.POST.get("search"))
    elif "srchByPD" in request.POST:
        get_cleaner = cleaners.objects.filter(preferred_day=request.POST.get("search"))
    elif "srchByType" in request.POST:
        get_cleaner = cleaners.objects.filter(type=request.POST.get("search"))
    elif "srchByDateAdded" in request.POST:
        get_cleaner = cleaners.objects.filter(date_added=request.POST.get("search"))
    context = {"cleaner_info": get_cleaner}
    return render(request, "cleaners/dashboard.html", context)


@login_required(login_url="/login_form/")
def create_status(request):
    form = statusForm()
    if request.method == "POST":
        form = statusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cleaners:create_cleaners")
    context = {"form": form}
    return render(request, "cleaners/create_status.html", context)


def updateStatus(request, pk):
    form = updateStatusForm()
    if request.method == "POST":
        new_status = request.POST["status"]
        cleaners.objects.filter(pk=pk).update(status=new_status)
        return redirect("cleaners:dashboard")
    context = {"form": form}
    return render(request, "cleaners/update_status.html", context)


# --------------------------------------------------------------------------------------------------------


def email_sending_system(request, pk):
    form = sent_emailForm()
    get_the_data = cleaners.objects.get(id=pk)
    if request.method == "POST":
        if "send_email" in request.POST:
            form = sent_emailForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                sent_to = Email_add.objects.get(client_add=get_the_data.email)
                subject = form.cleaned_data.get("email_subject")
                email_body = form.cleaned_data.get("email_body")
                instance.email_add = sent_to
                instance.save()
                from_email = settings.EMAIL_HOST_USER
                to_email = (get_the_data.email, "")
                message = EmailMultiAlternatives(
                    subject=subject, body=email_body, from_email=from_email, to=to_email
                )
                message.content_subtype = "html"
                message.send()
                return redirect("cleaners:email_record", pk=get_the_data.email)
            else:
                print(form.errors)
    context = {"form": form, "cleaners_data": get_the_data}
    return render(request, "cleaners/send_emails.html", context)


def previous_emails(request, pk):
    get_record = email_content.objects.filter(email_add__client_add=pk).values(
        "id", "email_subject"
    )
    context = {"all_emails": get_record, "email_add": pk}
    return render(request, "cleaners/email_record.html", context)


def email_details_of_a_specific_client(request, pk):
    get_record = email_content.objects.filter(id=pk).values("email_body")
    context = {"email_body": get_record}
    return render(request, "email_details.html", context)


# ---------------------------------------------------------------------------------------------------------------


def create_message(cleaners_name, staff_name, to_number):
    account_sid = account_sid
    auth_token = auth_token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hi, "
        + cleaners_name
        + " your profile has been created by "
        + staff_name
        + " at maid2clean",
        from_="+447862127546",
        to=to_number,
    )

    print(message.error_message)
    return "success"


# -----------------------------------------------------------------------------------------------------------------
