from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings

import os
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from cleaners.models import cleaners
from clients.models import clients, email_content, Email_add, ex_cleaner
from django.db.models import Q

from .forms import clientsForm, statusForm, sent_emailForm

from twilio.rest import Client

from dotenv import load_dotenv

import xlwt

# To get the tokens from .env file

load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

# ---------------------------------------------
# Creating the Profile of Clients


@login_required(login_url="/accounts/login/")
def create_clients(request):
    title_of_page = "Create Clients"
    current_date = {"get_date": str(datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))}
    form = clientsForm(initial=current_date)
    if request.method == "POST":
        form = clientsForm(request.POST, request.FILES)
        if form.is_valid():

            # We have to assign a cleaner to a client that's why we are assigning it through thsis custom code

            # The Problem Statement is, we have to list down available cleaners form a post code(Which is the post code of the Client)
            # and we are doing it dynamically using HTMX library

            # commit=False will stop the form from creating the data in the DB
            instance = form.save(commit=False)
            # Getting the ID of Cleaner Based on the Email Selected By the User
            cleaner_id = request.POST.get("list_of_cleaners", False)
            # Now Checking if the data is empty or not
            if cleaner_id != False:
                # If not empty then get the object of the cleaner and assign that object with cleaner_allocated Field
                c_info = cleaners.objects.get(id=cleaner_id)
                instance.cleaner_allocated = c_info
                # At last save the Post Code, because we have also excluded it from the form and altered the input field that's why we have to
                # assign it manually
                instance.post_code = request.POST["post_code"]
                instance.save()
                # We will add a cleaner into the ex_cleaner db to keep the record of cleaners allocated to this client
                ex_cl = ex_cleaner.objects.create(
                    client_email=request.POST.get("email"),
                    client_id=instance.id,
                    cleaner=c_info,
                )
                ex_cl.save()
            elif cleaner_id == False:
                """If Data is Empty then just write the post code and cleaners_allocated field will be empty"""
                instance.post_code = request.POST["post_code"]
                instance.save()
                # Sending SMS using Twilio API
            try:
                create_message(
                    request.POST["name"],
                    request.user.get_username(),
                    request.POST["mobile_number"],
                )
            except:
                print("cannot send the sms in clients")
            finally:
                return redirect("clients:dashboard")

    context = {"form": form, "title": title_of_page}
    return render(request, "clients/create_clients.html", context)


def update_client(request, pk):
    obj = clients.objects.get(id=pk)
    current_date = {"get_date": str(datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))}
    form = clientsForm(instance=obj, initial=current_date)
    if request.method == "POST":
        form = clientsForm(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            cleaner_id = request.POST.get("list_of_cleaners", False)
            instance.save()
            if cleaner_id != False:
                c_info = cleaners.objects.get(id=cleaner_id)
                # We will add a cleaner into the ex_cleaner db to keep the record of cleaners allocated to this client
                ex_cl = ex_cleaner.objects.create(
                    client_email=request.POST.get("email"),
                    client_id=instance.id,
                    cleaner=c_info,
                )
                ex_cl.save()
            elif cleaner_id == False:
                """If Data is Empty then just write the post code and cleaners_allocated field will be empty"""
                instance.post_code = request.POST["post_code"]
                instance.save()
            return redirect("clients:dashboard")
    context = {"form": form}
    return render(request, "clients/create_clients.html", context)


"""A Simple view function to create the status data in the database, It's a feature to allow user to add multiple data in the DB """


@login_required(login_url="/accounts/login/")
def create_status(request):
    form = statusForm()
    if request.method == "POST":
        form = statusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clients:create_clients")
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, "clients/create_status.html", context)


# ---------------------------------------------------------------------------------------------------------------------------------------------

"""It is a function for the HTMX library to get the id and email of the cleaner based on the post code"""


def show_cleaner_to_client(request):
    get_data = cleaners.objects.filter(post_code=request.POST.get("post_code")).values(
        "id", "email"
    )
    context = {"cleaners_list": get_data}
    return render(request, "clients/cleaners_list.html", context)


# ----------------------------------------------------------------------------------------------------------------------------------------------
""" A Simple Dashboard to filter some data about Clients"""


@login_required(login_url="/accounts/login/")
def clients_dashboard(request):
    get_client = clients.objects.all()
    if "srchByName" in request.POST:
        get_client = clients.objects.filter(name=request.POST.get("search"))
    elif "srchByEmail" in request.POST:
        get_client = clients.objects.filter(email=request.POST.get("search"))
    elif "srchByZip" in request.POST:
        get_client = clients.objects.filter(post_code=request.POST.get("search"))
    elif "srchByPD" in request.POST:
        get_client = clients.objects.filter(preferred_day=request.POST.get("search"))
    elif "srchByType" in request.POST:
        get_client = clients.objects.filter(type=request.POST.get("search"))
    elif "srchByDateAdded" in request.POST:
        get_client = clients.objects.filter(date_added=request.POST.get("search"))

    context = {"client_info": get_client}
    return render(request, "clients/dashboard.html", context)


# -----------------------------------------------------------------------------------------------------------------------
"""An advance filtring system to filter out the data based on the query by the user, and at the end it will generate a .xls file as a report"""
# Checking out if the value is empty or not
def is_valid_query_param(param):
    return param != "" and param is not None


@login_required(login_url="/accounts/login/")
def search_by_filter(request):
    query = clients.objects.all()
    if request.method == "POST":
        search_by_email = request.POST.get("search_by_email")
        status_q = request.POST.get("status")
        pref_day = request.POST.get("pref_day")
        Post_code = request.POST.get("Post_code")
        type_q = request.POST.get("type")
        frequency = request.POST.get("frequency")
        number_of_hours = request.POST.get("number_of_hours")

        min_date = request.POST.get("fromDate")
        max_date = request.POST.get("toDate")

        if is_valid_query_param(search_by_email):
            query = query.filter(Q(email=search_by_email)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(status_q):
            query = query.filter(Q(status__abber_of_notes=status_q)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(pref_day):
            query = query.filter(Q(preferred_day=pref_day)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(Post_code):
            query = query.filter(Q(post_code=Post_code)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(type_q):
            query = query.filter(Q(type=type_q)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(number_of_hours):
            query = query.filter(Q(number_of_hours=number_of_hours)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(frequency):
            query = query.filter(Q(frequency=frequency)).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(min_date):
            query = query.filter(date_added__gte=min_date).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        if is_valid_query_param(max_date):
            query = query.filter(date_added__lt=max_date).values_list(
                "name",
                "address_line_1",
                "address_line_2",
                "address_line_3",
                "post_code",
                "landline_number",
                "mobile_number",
                "email",
                "date_added",
                "status__abber_of_notes",
                "preferred_day",
                "type",
                "frequency",
                "number_of_hours",
                "paying",
                "paying_methods",
                "cleaner_allocated__name",
                "payment_reference",
            )

        # Creating the xls report using xlwt library
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = (
            'attachment; filename="clients_report"'
            + str(datetime.datetime.now())
            + ".xls"
        )

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("Filtered_data")
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = [
            "Name",
            "Address Line 1",
            "Address Line 2",
            "Address Line 3",
            "Post Code",
            "Landline Number",
            "Mobile Number",
            "Email",
            "Date Added",
            "Status",
            "Preferred Day",
            "Type",
            "Frequency",
            "Number of Hours",
            "Paying?",
            "Paying Method",
            "Cleaner Allocated",
            "Payment Reference",
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        for row in query:
            row_num += 1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)

        wb.save(response)

        return response

    return render(request, "clients/searching/search_by_filter.html")


# -----------------------------------------------------------------------------------------------------------------------
"""Sending Custom Emails to clients"""


@login_required(login_url="/accounts/login/")
def email_sending_system(request, pk):
    form = sent_emailForm()
    # This single line will get the email address from the dashboard and will be use as the receiver's email
    get_the_data = clients.objects.get(id=pk)

    if request.method == "POST":
        if "send_email" in request.POST:
            form = sent_emailForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                # Saving emails sent to a specific email address to get the list of emails sent to client
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
                return redirect("clients:email_record", pk=get_the_data.email)
    context = {"form": form, "clients_data": get_the_data}
    return render(request, "clients/send_emails.html", context)


"""Getting the list of emails sent to a specific client"""


@login_required(login_url="/accounts/login/")
def previous_emails(request, pk):
    get_record = email_content.objects.filter(email_add__client_add=pk).values(
        "id", "email_subject"
    )
    context = {"all_emails": get_record, "email_add": pk}
    return render(request, "clients/email_record.html", context)


"""Detail of an email e.g subject, body"""


@login_required(login_url="/accounts/login/")
def email_details_of_a_specific_client(request, pk):
    get_record = email_content.objects.filter(id=pk).values(
        "email_subject", "email_body"
    )
    context = {"email_body": get_record}
    return render(request, "email_details.html", context)


# SMS System

"""Custom Function to send the SMS to a client. NOTE: We're sending the sms on profile creation"""


def create_message(clients_name, staff_name, to_number):
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hi, "
        + clients_name
        + " your profile has been created by "
        + staff_name
        + " at maid2clean",
        from_="+447862127546",
        to=to_number,
    )
    return "success"


# ---------------------------------------------------------------------------------------

"""A single template to show the profile of a client"""


def profile_template(request, pk):
    get_client = clients.objects.get(id=pk)
    get_ex_cleaner = ex_cleaner.objects.filter(client_id=pk).values("cleaner__name")
    context = {"client_info": get_client, "ex_cleaner": get_ex_cleaner}
    return render(request, "clients/profile_view/template.html", context)


# ----Extra function needs to delete at the final commit-----
def create_pdf(request, pk):
    c_info = clients.objects.get(id=pk)
    template_path = "clients/create_report/export_pdf.html"
    context = {"client_detail": c_info}
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="client_profile.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
