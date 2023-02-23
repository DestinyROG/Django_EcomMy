from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def Resister(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('This username is taken.')
                # messages.info(request,'This username is taken.')
                
            else:
                User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                # messages.info(request,'You resistered succesfully')
                return redirect("/")


def Login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already loged in.')
        return redirect('/')
    else:
        if request.method =='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user != None:
                login(request,user=user)
                messages.info(request,'You Loged in succesfully')
                return redirect("/")
            else:
                messages.error(request,'user not exist')
                return redirect('/')


def Logout(request):
    logout(request)
    messages.info(request,'Your account is loged out successfully.')
    return redirect('/')

def Delete(request):
    User.delete(self=request.user)
    messages.info(request,'Your account is deleted successfully.')
    return redirect('/')

