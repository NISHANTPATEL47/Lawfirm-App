from django.shortcuts import render,redirect
from registrationapp.forms import UserForm,UserProfileForm,UserUpdateForm,UserProfileUpdateForm
from lawfirmapp.models import Appointment,Case_management
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered =  False
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            # print(form.cleaned_data['username'])
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user # we are merging the two models
            profile.save()
            registered =True
    else:
        form = UserForm()    
        form1 = UserProfileForm()    

    context={
        'form': form,
        'form1': form1,
        'registered':registered
    }
    return render(request,"registration.html",context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        # print(username)
        # print(password)
        
        user = authenticate(username=username,password= password)
        if user:
            if user.is_active:
                login(request , user)
                return redirect('home')
        else:
            return HttpResponse("Plz check your cred..!!!")
    return render(request , "login.html",{})



@login_required(login_url='login')
def home(request):
    return render(request , "home.html",{})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    appointment = Appointment.objects.filter(user=request.user).prefetch_related('appointments__lawyer')
    return render(request,"userprofile.html",{'appointment':appointment})


@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        form1 = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()
            profile = form1.save(commit=False)
            profile.user = user # we are merging the two models
            profile.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        form1=UserProfileUpdateForm(instance=request.user.userprofile)
        

    return render(request,"update.html",{'form':form,'form1':form1})

