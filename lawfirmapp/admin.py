from django.contrib import admin
from lawfirmapp.models import Lawyerdetails ,Casedetails,Enquiry,Appointment,Case_management

# Register your models here.
admin.site.register(Lawyerdetails)
admin.site.register(Casedetails)
admin.site.register(Enquiry)
admin.site.register(Appointment)
admin.site.register(Case_management)