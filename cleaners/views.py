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
from django.db.models import Q
from django.http import HttpResponse

from django.template.loader import get_template

from django.conf import settings

import xlwt
from datetime import datetime

# to get the token from .env files
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

# -------------------------------------------------------------------------------------------------------
@login_required(login_url="/login_form/")
def create_cleaners(request):
    title_of_page = "Create Cleaners"
    current_date = {"get_date": str(datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))}
    form = cleanersForm(initial=current_date)
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


def update_cleaner(request, pk):
    obj = cleaners.objects.get(id=pk)
    current_date = {"get_date": str(datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))}
    form = cleanersForm(initial=current_date, instance=obj)
    if request.method == "POST":
        form = cleanersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("cleaners:dashboard")
    context = {"form": form}
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


# -----------------------------------------------------------------------------------------------------------------------------------


def is_valid_query_param(param):
    return param != "" and param is not None


def search_by_filter(request):
    query = cleaners.objects.all()
    if request.method == "POST":
        c_email = request.POST.get("search_by_email")
        c_status = request.POST.get("status")
        c_permit_to_work_needed = request.POST.get("permit_to_work_needed")
        c_smoker = request.POST.get("is_smoker")
        c_iron = request.POST.get("can_iron")
        c_drive = request.POST.get("is_driver")
        c_car = request.POST.get("has_car")
        c_post_code = request.POST.get("Post_code")
        c_areas_worked = request.POST.get("areas_worked")
        c_convict_of_offence = request.POST.get("prev_convicted_of_offence")
        c_number_of_hours = request.POST.get("number_of_hours")
        c_pet_allergies = request.POST.get("pet_allergies")

        min_date = request.POST.get("fromDate")
        max_date = request.POST.get("toDate")

        if is_valid_query_param(c_email):
            query = query.filter(Q(email=c_email)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_status):
            query = query.filter(Q(status__abber_of_notes=c_status)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_permit_to_work_needed):
            query = query.filter(
                Q(permit_to_work_needed=c_permit_to_work_needed)
            ).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_smoker):
            query = query.filter(Q(smoker=c_smoker)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_iron):
            query = query.filter(Q(can_iron=c_iron)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_drive):
            query = query.filter(Q(driver=c_drive)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_car):
            query = query.filter(Q(has_car=c_car)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_post_code):
            query = query.filter(Q(post_code=c_post_code)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_areas_worked):
            query = query.filter(Q(areas_worked=c_areas_worked)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_convict_of_offence):
            query = query.filter(
                Q(prev_convicted_of_offence=c_convict_of_offence)
            ).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_number_of_hours):
            query = query.filter(
                Q(number_of_hours_wanted=c_number_of_hours)
            ).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(c_pet_allergies):
            query = query.filter(Q(pet_allergies=c_pet_allergies)).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(min_date):
            query = query.filter(date_added__gte=min_date).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        if is_valid_query_param(max_date):
            query = query.filter(date_added__lt=max_date).values_list(
                "name",
                "post_code",
                "mobile_number",
                "date_added",
                "status__abber_of_notes",
                "number_of_hours_wanted",
                "nationality",
                "permit_to_work_needed",
                "NI_Number",
                "consent_for_DBS",
                "smoker",
                "can_iron",
                "driver",
                "has_car",
                "areas_worked",
                "prev_work_experience",
                "prev_convicted_of_offence",
                "pet_allergies",
                "type_of_allergy",
            )

        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = (
            'attachment; filename="cleaners_report"'
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
            "Post code",
            "Mobile number",
            "Date added",
            "Status",
            "Req Hours",
            "Nationality",
            "Permit Needed?",
            "NIN",
            "DBS",
            "Smoker",
            "Iron",
            "Driver",
            "Car",
            "Areas",
            "Work exp",
            "Convicted",
            "Allergies",
            "Type of Allergy",
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

    return render(request, "cleaners/searching/search_by_filter.html")


# -----------------------------------------------------------------------------------------------------------------------------------


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
def profile_template(request, pk):
    get_cleaner = cleaners.objects.get(id=pk)
    context = {"cleaner_info": get_cleaner}
    return render(request, "cleaners/profile_view/template.html", context)


# -----------------------------------------------------------------------------------------------------------------


def permit_image(request):
    if request.method == "POST":
        answer = ""
        if request.POST.get("permit_to_work_needed") == "Yes":
            answer = "Yes"
        else:
            answer = "No"
    context = {"answer": answer}
    return render(request, "cleaners/partials/permit_image.html", context)


def pet_allergies(request):
    if request.method == "POST":
        answer = ""
        if request.POST.get("pet_allergies") == "Yes":
            answer = "Yes"
        else:
            answer = "No"
    context = {"answer": answer}
    return render(request, "cleaners/partials/allergy_type.html", context)
