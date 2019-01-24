from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from . import forms
from .models import *



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
        else:
            error_message = "Wrong Password or Username"
            return render(request,'core/login.html',{'error_message': error_message})


def successLogin(request):
    return redirect('core:user_profile_page', user_name = request.user.username)

def RegistrationView(request):

    if request.method == "GET":
        return render(request, 'core/register.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        emailid = request.POST['emailid']


        if not (User.objects.filter(username=username).exists()):
            user = User.objects.create_user(username, emailid, password)
            UserProfile.objects.create(user=user)


        else:

            error_message = "The user already exists!"
            return render(request, 'core/register.html', {'error_message': error_message})


        return redirect('core:login')


def displayUserProfile(request,user_name):
    user = User.objects.get(username=user_name)
    current_user = User.objects.get(username=request.user.username)
    if current_user.userprofile.follows.filter(user=user).exists():
        follows = "Unfollow"
    else:
        follows = "Follow"
    return render (request, 'core/profile.html', {'user': user, 'follow': follows})



def editProfile(request, user_name):
    user = User.objects.get(username=user_name)
    if request.method=='POST':
       user.userprofile.bio = request.POST['bio']
       if request.POST['password']:
           user.set_password(request.POST['password'])

       user.userprofile.city = request.POST['city']
       user.userprofile.country = request.POST['country']
       user.save()
       user.userprofile.save()
       return redirect('core:user_profile_page', user_name = user.username)


def userLogout(request):
    logout(request)
    return redirect('core:login')


def userFollow(request, user_name):
    user_to_follow = User.objects.get(username=user_name)
    current_user = User.objects.get(username=request.user.username)
    current_user.userprofile.follows.add(user_to_follow.userprofile)
    #current_user.userprofile.save()
    return redirect('core:user_profile_page', user_name=user_to_follow.username)

def create_post(request,user_name):
    if request.method == "POST":
        newpost = Post()
        newpost.author = User.objects.get(username=user_name)
        newpost.content = request.POST["content"]
        newpost.save()

        return redirect('core:user_profile_page',user_name=user_name)

def userUnfollow(request, user_name):
    user_to_unfollow = User.objects.get(username=user_name)
    current_user = User.objects.get(username=request.user.username)
    current_user.userprofile.follows.remove(user_to_unfollow.userprofile)
    return redirect('core:user_profile_page', user_name = user_to_unfollow.username)

def createComment(request, user_name, post_id):
    if request.method == "POST":
        post_for_comment = Post.objects.get(id = post_id)
        Comment.objects.create(author=request.user, post=post_for_comment, content= request.POST['comment'])
        return redirect('core:user_profile_page', user_name = user_name)

def displayFeed(request):
    current_user = User.objects.get(username=request.user.username).userprofile
    posts = Post.objects.filter(author=current_user.follows.all().values('user')).order_by('published_date')
    return render(request, 'core/feed.html', {'user': request.user, 'posts': posts})







