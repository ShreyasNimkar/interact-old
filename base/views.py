from nturl2path import url2pathname
from django.shortcuts import redirect, render
from django.http import HttpResponse
from user.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def starthandler(request):
    if request.GET['start']=='Sign Up':
        return signup(request)
    else:
        return log_in(request)
def index(request):
    if request.user.is_authenticated:
        return redirect('user/feed')
    return render(request,'homepage.html')

def signup(request):
    return render(request,'signup.html')

def log_in(request):
    return render(request,'login.html')

def signuphandler(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        age=request.POST['age']
        user=User.objects.create_user(username,password,fname,email)
        user.last_name=lname
        user.age=age
        user.is_active=True
        user.save()
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            url='/user/feed/'
            return redirect(url)
        else:
            return HttpResponse("User does not exist")

def log_inhandler(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user is not None:
            user.is_active=True
            user.save()
            login(request,user)
            url='/user/feed/'
            return redirect(url)
        else:
            return HttpResponse("User does not exist")
    else:
        return HttpResponse("Error")

def log_out(request):
    logout(request)
    return redirect('/')