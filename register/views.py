from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from .models import Users
# Create your views here.
def register(request):
    isUserLoggedIn = False
    if(request.session.get("isLoggedIn")):
        isUserLoggedIn = (request.session["isLoggedIn"]=="T")
    if(isUserLoggedIn):
        return HttpResponseRedirect(reverse('home-index'))
    if(request.method=='POST'):
        u = Users(username=request.POST["fName"], email=request.POST["email"], password=request.POST["pwd"], fname=request.POST["lName"])
        u.save()
    return TemplateResponse(request, "register/register.html", {'title': 'Register'})

def login(request):
    Message = "One or More Field is Empty"
    if(request.method=='POST'):
        if(not request.POST["uName"]=="" and not request.POST["pwd"]==""):
            res = Users.objects.filter(username=request.POST["uName"],
                                    password=request.POST["pwd"])
            if(res):
                Message = "S"
                request.session["isLoggedIn"] = "T"
                request.session["user"] = request.POST["uName"]
            else:
                Message = "F"
    request.session["login_message"] = Message
    return HttpResponseRedirect(reverse('home-index'))

def logout(request):
    print("Logout Called")
    request.session.flush()
    request.session["isLoggenIn"] = "F"
    return HttpResponseRedirect("/home")
