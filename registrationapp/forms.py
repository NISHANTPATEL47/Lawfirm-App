from django import forms
from django.contrib.auth.models import User
from registrationapp.models import UserProfile
from django_recaptcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        # fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','street','city','state','zipcode','profile_pic']
    captcha = ReCaptchaField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','street','city','state','zipcode','profile_pic']

    
    