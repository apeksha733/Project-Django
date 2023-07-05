from django.shortcuts import render,redirect
from myapp.models import Contact
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.

def index(Request):
    #return HttpResponse("This is home page default :This is when blank is passed .... use/myapp or /home")
    #return render(Request,'index.html')            #after adding a template
    context={"variable":"This is a variable i am sending" }
    if Request.user.is_anonymous:
        return redirect("/login")

    return render(Request, 'index.html', context)

def about(Request):
    #return HttpResponse("This is my first app.This is about page")
    return render(Request, 'about.html')

def services(Request):
    #return HttpResponse("This is Services page")
    return render(Request, 'services.html')

def contact(Request):
    #return HttpResponse("This is Contact page")
    if Request.method=="POST":
        first_name = Request.POST.get('first_name')
        last_name =Request.POST.get('last_name')
        phone_number =Request.POST.get('phone_number')
        email =Request.POST.get('email')
        type =Request.POST.get('type')
        user_input = Request.POST.get('user_input')

        contact=Contact(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,type=type,user_input=user_input)
        contact.save()
        messages.success(Request, "Your message has reached Us.Thanks for your time!")
    return render(Request, 'contact.html')

def loginuser(Request):
    if Request.method=="POST":
        username =Request.POST.get('username')
        password = Request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(Request,user)
            return redirect("/")
        else:
            return render(Request, 'login.html')

    #return HttpResponse("This is Services page")
    return render(Request, 'login.html')

def logoutuser(Request):
    #return HttpResponse("This is Services page")
    logout(Request)
    return redirect("/login")