from django.contrib import messages
from django.shortcuts import render
from .forms import inquiryForm


def inquiryView(request):
    title = "Inquiry"
    form = inquiryForm()
    if request.method == "POST":
        form = inquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Inquiry has been submitted Successfully, We will contact you soon')
    context = {'form':form, 'title': title}
    return render(request, 'inquiry/inquiry.html', context)
