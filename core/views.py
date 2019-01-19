from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from . import forms
from .models import UserProfile



# Create your views here.


def LoginView(request):
    if request.method == "GET":
        return render(request, 'core/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('core:login-success')


def successLogin(request):
    return HttpResponse('Your login was a success!')


def RegistrationView(request):

    if request.method == "GET":
        return render(request, 'core/register.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        emailid = request.POST['emailid']


        if not (User.objects.get(username=username)):

            user = User(username=username, password=password, email=emailid)
            user.save()
            userprofile = UserProfile(User = user)
            userprofile.save()


        else:

            error_message = "The user already exists!"
            return render(request, 'core/register.html', {'error_message': error_message})


        return redirect('core:login')





