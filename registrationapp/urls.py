from django.urls import path
from registrationapp import views

urlpatterns=[
    path('',views.register, name='register'),
    path('home',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update'),
]  