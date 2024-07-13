# Create your views here.
from django.contrib import admin , messages # type: ignore
from django.urls import path , include # type: ignore
from django.http import HttpResponse # type: ignore
from django.shortcuts import render , redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate,login,logout # type: ignore
from home.models import Course


def HomeAPI(request):
    return render(request, "home.html")


def Signup(request):
    if request.method == "POST":
        # print(request.POST.get("username"))
        # print(request.POST.get("password"))
        # print(request.POST.get("first_name"))
        # print(request.POST.get("last_name"))

        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name) # type: ignore

        messages.success(request,"You have been Signed Up Successfully")
        messages.warning(request,"But you have to logIn to Enter")
        
        return redirect("/login")
        # DBs
    return render(request, "signup.html")

def LogIn(request):
    if request.method == "POST":
        print(request.POST.get("username"))
        print(request.POST.get("password"))

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,"You have logged In Successfully")
            return redirect("/")

        messages.warning(request,"Invalid Username or Password")
        return redirect("/login")
    return render(request, "login.html")

def ChangePassword(request):
    if request.method == "POST":
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        print("oldpassword",oldpassword)
        print("newpassword",newpassword)
        # print(request.POST.get("confirm password"))
        
        # confirmpassword = request.POST.get("confirm password")
        username = request.user.username

        user = User.objects.get(username=username)
        
        if user.check_password(oldpassword):
            user.set_password(newpassword)
            user.save()
            messages.success(request,"Your password has been changed successfully")
            return redirect("/")
        messages.warning(request,"Invalid old password. Please try again")
        return redirect("/changepassword")
    return render(request,"changepassword.html")


def LogOut(request):
    logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect("/")

def courses(request):
    my_courses = Course.objects.all()
    # for course in my_courses:
    #     print(course.title, course.category)

    return render(request,"courses.html",{"courses": my_courses})