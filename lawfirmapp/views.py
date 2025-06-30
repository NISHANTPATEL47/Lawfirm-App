from django.shortcuts import render,redirect
from lawfirmapp.models import Lawyerdetails,Casedetails,Appointment,Case_management
from registrationapp.forms import UserForm
from lawfirmapp.forms import enquiryform,appointmentform
from django.contrib.auth.decorators import login_required
from lawfirmapp.utils import send_email_view

# Create your views here.
@login_required(login_url='login')
def lawfirm(request):
    lawfirm = Casedetails.objects.all()
    return render(request, "lawfirm.html", {'lawfirm': lawfirm})


@login_required(login_url='login')
def lawyers(request):
    lawyers = Lawyerdetails.objects.all()
    return render(request, "lawyers.html", {'lawyers': lawyers})


@login_required(login_url='login')
def enquiry(request):
    registered =  False
    if request.method == 'POST':
        form = enquiryform(request.POST,request.FILES)
        if form.is_valid():
            enquiry = form.save()
            enquiry.save()
            registered = True
    else:
        form = enquiryform() 

    context={
        'form': form,
        'registered':registered
    }        
    return render(request, "enquiry.html", context)


@login_required(login_url='login')
def appointment(request):
    registered =  False
    if request.method == 'POST':
        form = appointmentform(request.POST,request.FILES)
        if form.is_valid():
            print("Success") 
            email = form.cleaned_data['email']
            print(email)
            enquiry = form.save(commit=False)
            enquiry.user = request.user 
            enquiry.save()
            registered = True
            response = send_email_view(email)
            return response 
    else:
        form = appointmentform() 

    appointments = Appointment.objects.filter(user=request.user)  
    case_management = Case_management.objects.all()    

    context={
        'form': form,
        'registered':registered,
        'appointments': appointments,
        'case_management': case_management
    }        
    return render(request, "booking.html", context)


