from django import forms
from lawfirmapp.models import Lawyerdetails,Casedetails,Enquiry,Appointment
# class lawyerdetailsform(forms.ModelForm):
#     class Meta:
#         model = Lawyerdetails
#         fields = "__all__"

# class casedetailsform(forms.ModelForm):
#     class Meta:
#         model = Casedetails
#         fields = "__all__"

class enquiryform(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"

class appointmentform(forms.ModelForm):
    fees=forms.IntegerField(initial=500,disabled=True)
    class Meta:
        model = Appointment
        fields =['name','phone','email','address','case_type','description','casedoc','total_no_of_hearing','court_name','fees']