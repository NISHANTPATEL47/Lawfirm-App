from django.urls import path
from lawfirmapp import views

urlpatterns=[
    path('lawfirm/', views.lawfirm, name='lawfirm'),
    path('lawyers/', views.lawyers, name='lawyers'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('appointment/', views.appointment, name='appointment'),
]   