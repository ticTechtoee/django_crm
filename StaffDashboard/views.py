from django.shortcuts import redirect, render
from inquiry.models import Inquiry
from .forms import UpdateinquiryForm

def dashboard(request):
    title = "Staff"
    inquiry = Inquiry.objects.all()
    context = {'inquiry': inquiry, 'title': title}
    return render(request, 'StaffDashboard/dashboard.html', context)

def UpdateInquiry(request, pk):
    title = "Staff"
    obj = Inquiry.objects.get(id=pk)
    form = UpdateinquiryForm(instance = obj)
    if request.method == "POST":
        form = UpdateinquiryForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('StaffDashboard:staff_dashboard')
    context = {'form':form, 'title':title}
    return render(request, 'StaffDashboard/update_inquiry.html', context)
