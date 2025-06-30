from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lawyerdetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    yearofexperience = models.IntegerField()
    specialization = models.CharField(max_length=100)
    totalcases = models.IntegerField()
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='lawyerimg/',blank=True,null=True)

class Casedetails(models.Model):
    case_title = models.CharField(max_length=100)
    case_description = models.CharField(max_length=1000)
    case_image = models.ImageField(upload_to='caseimg/',blank=True,null=True)

case_types = [
    ('tax','TAX'),
    ('divorse','DIVORSE'),
    ('criminal','CRIMINAL'),
    ('civil','CIVIL'),
    ('family','FAMILY'),
    ('environmental','ENVIRONMENTAL'),
    ('bankruptcy','BANKRUPTY'),
    ('cild abuse','CHILD ABUSE'),
    ('constitutional','CONSTITUTIONAL'),
    ('administrative','ADMINISTRATIVE'),
    ('contract','CONTRACT'),
    ('tort','TORT'),
    ('property','PROPERTY'),
    ('intellectual property','INTELLECTUAL PROPERTY'),
    ('probate','PROBATE'),
]

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    anydoc = models.ImageField(upload_to='document/',blank=True,null=True)
    case_type = models.CharField(max_length=100,choices=case_types,default='Tax Law')

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100,choices=case_types,default='tax')
    description = models.CharField(max_length=1000)
    casedoc = models.ImageField(upload_to='appointmentimg/',blank=True,null=True)
    total_no_of_hearing = models.IntegerField()
    court_name = models.CharField(max_length=100)
    fees = models.IntegerField()

class Case_management(models.Model):  
    case_type = models.ForeignKey(Appointment,related_name='appointments',on_delete=models.CASCADE)    
    lawyer = models.ForeignKey(Lawyerdetails,related_name='lawyerdetail',on_delete=models.CASCADE)    
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)    